import json
import xml.etree.ElementTree as ET
from typing import Optional, Any, List, Dict

from fastapi import File
from fastapi import HTTPException

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.contracts.departments_repository_contract import DepartmentsRepositoryContract
from src.core.contracts.semesters_repository_contract import SemestersRepositoryContract
from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.converters import entity_to_model, entity_to_model_list
from src.core.entities.syllabus.syllabus import Syllabus
from src.core.exceptions.db_exceptions import DatabaseError
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.teacher_course_service_contract import TeacherCourseServiceContract
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract
from src.features.syllabus.syllabus_utils.xml_utils import parse_syllabus, create_template
from src.models.semester import SemesterOut
from src.models.syllabus.syllabus_models import SyllabusParsed, SyllabusIn, Course, Semester, SyllabusOut


class SyllabusService(SyllabusServiceContract):
    def __init__(
            self,
            syllabus_repository: SyllabusRepositoryContract,
            departments_repository: DepartmentsRepositoryContract,
            courses_repository: CoursesRepositoryContract,
            semesters_repository: SemestersRepositoryContract,
            teachers_course_service: TeacherCourseServiceContract
    ):
        self.repository = syllabus_repository
        self.departments_repository = departments_repository
        self.courses_repository = courses_repository
        self.semesters_repository = semesters_repository
        self.teachers_course_service = teachers_course_service

    async def save(self, file: File(...)) -> SyllabusParsed:
        try:
            contents = await file.read()
            root = ET.fromstring(contents)
            syllabus = parse_syllabus(root)

            department = await self.departments_repository.get_department_by_code(
                department_code=syllabus.department_code)
            if not department:
                raise NotFoundException(detail="Department not found!")

            for semester in syllabus.semesters:
                semester_in_db = await self.semesters_repository.get_semester_by_year_and_number(
                    department=department.id, year=1, number=1)
                if not semester_in_db:
                    raise NotFoundException(detail="Semester not found!")

                for course in semester.courses:
                    course_in_db = await self.courses_repository.get_course_by_code(
                        course_code=course.course_code,
                        department_id=department.id
                    )

                    if not course_in_db:
                        raise NotFoundException(detail="Course not found!")

            return await self.repository.save(department_id=department.id, syllabus=syllabus)

        except ET.ParseError:
            raise HTTPException(status_code=400, detail="Invalid XML format.")

    async def get_course_list(self, department_id: int) -> list[dict[str, Any]]:
        syllabus = await self.repository.get_by_department(department_id)

        result = []
        for semester in syllabus.semesters:
            semester_data = await self.semesters_repository.get_semester_by_year_and_number(
                department=department_id,
                year=semester.year,
                number=semester.number,
            )
            for course in semester.courses:
                course_data = await self.teachers_course_service.get_teacher_course_by_course_code(
                    department_id=department_id, course_code=course.course_code)

                result.append(
                    {
                        "semester": SemesterOut(**semester_data.model_dump()),
                        "course": course_data.course,
                        "teacher": course_data.teacher
                    }
                )

        return result

    async def get_by_department_id(self, department_id) -> Optional[SyllabusParsed]:
        return await self.repository.get_by_department(department_id)

    async def getByDeptIDAndSemesterCode(self, department_id: int, semester_code: int) -> Optional[SyllabusParsed]:
        return await self.repository.getByDeptIDAndSemesterCode(department_id, semester_code)

    async def updateSyllabus(self, department_id: int, semester_code: int, course_code: str, course_type: str) -> \
            Optional[SyllabusParsed]:
        return await self.repository.updateSyllabus(department_id, semester_code, course_code, course_type)

    async def template(self, department_id: int) -> Optional[Any]:
        department = await self.departments_repository.get_by_id(department_id)

        semesters = await self.semesters_repository.get_semesters_by_department_id(department_id)

        return create_template(
            department_code=department.code,
            department_name=department.name,
            semesters_list=semesters
        )

    async def get_all_syllabuses(self, page: int = 1, page_size: int = 10, paginate: bool = False) -> Dict[str, Any]:
        syllabuses = []
        syllabuses_in_db = await self.repository.get_all()
        for item in syllabuses_in_db["items"]:
            syllabuses.append(
                SyllabusOut(
                    department_id=item.department_id,
                    syllabus=SyllabusParsed(**item.syllabus)
                )
            )

        return {"items": syllabuses}

    async def create_syllabus(self, syllabus_in: SyllabusIn) -> Optional[SyllabusParsed]:
        syllabus_parsed = await self.convert_syllabus_in(syllabus_in)

        syllabus = await self.repository.create(
            Syllabus(
                department_id=syllabus_in.department_id,
                syllabus=syllabus_parsed.model_dump()
            )
        )
        if not syllabus:
            raise DatabaseError()

        return syllabus_parsed

    async def update_syllabus(self, id: int, syllabus_in: SyllabusIn) -> Optional[SyllabusParsed]:
        syllabus_parsed = await self.convert_syllabus_in(syllabus_in)
        syllabus = await self.repository.update(
            id=id,
            obj_data=Syllabus(
                department_id=syllabus_in.department_id,
                syllabus=syllabus_parsed.model_dump()
            )
        )

        if not syllabus:
            raise DatabaseError()

        return syllabus_parsed

    async def convert_syllabus_in(self, syllabus_in: SyllabusIn) -> Optional[SyllabusParsed]:
        department_in_db = await self.departments_repository.get_by_id(syllabus_in.department_id)
        if not department_in_db:
            NotFoundException(detail="Department not found!")

        semesters = []

        for semester in syllabus_in.semesters:
            semester_in_db = await self.semesters_repository.get_by_id(semester.id)
            if not semester_in_db:
                NotFoundException(detail="Semester not found!")

            courses = []
            for course in semester.courses:
                course_in_db = await self.courses_repository.get_by_id(course.id)
                if not course_in_db:
                    NotFoundException(detail="Course not found!")

                courses.append(
                    Course(
                        course_code=course_in_db.code,
                        title=course_in_db.title,
                        credit=course.credit,
                        prerequisite=course.prerequisite,
                        type=course_in_db.course_type,
                        contact_hours=course.contact_hours,
                        rationale=course.rationale,
                        course_objectives=course.course_objectives,
                        outcomes=course.outcomes,
                        course_description=course.course_description,
                        recommended_books=course.recommended_books,
                        hardware_software_requirements=course.hardware_software_requirements,
                    )
                )
            pass

            semesters.append(
                Semester(
                    year=semester_in_db.year,
                    number=semester_in_db.number,
                    courses=courses
                )
            )
        pass

        return SyllabusParsed(
            department_code=department_in_db.code,
            department_name=department_in_db.name,
            semesters=semesters
        )
