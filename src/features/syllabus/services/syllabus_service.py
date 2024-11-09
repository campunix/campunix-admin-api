import xml.etree.ElementTree as ET
from typing import Optional, Any

from fastapi import File
from fastapi import HTTPException

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.contracts.departments_repository_contract import DepartmentsRepositoryContract
from src.core.contracts.semesters_repository_contract import SemestersRepositoryContract
from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract
from src.features.syllabus.syllabus_utils.xml_utils import parse_syllabus, create_template
from src.models.syllabus.syllabus_models import SyllabusParsed


class SyllabusService(SyllabusServiceContract):
    def __init__(
            self,
            syllabus_repository: SyllabusRepositoryContract,
            departments_repository: DepartmentsRepositoryContract,
            courses_repository: CoursesRepositoryContract,
            semesters_repository: SemestersRepositoryContract
    ):
        self.repository = syllabus_repository
        self.departments_repository = departments_repository
        self.courses_repository = courses_repository
        self.semesters_repository = semesters_repository

    async def save(self, file: File(...)) -> SyllabusParsed:
        try:
            contents = await file.read()
            root = ET.fromstring(contents)
            syllabus = parse_syllabus(root)

            department = await self.departments_repository.get_department_by_code(department_code=syllabus.DepartmentCode)
            if not department:
                raise NotFoundException(detail="Department not found!")

            for semester in syllabus.Semesters:
                semester_in_db = await self.semesters_repository.get_semester_by_year_and_number(year=1, number=1)
                if not semester_in_db:
                    raise NotFoundException(detail="Semester not found!")

                for course in semester.Courses:
                    course_in_db = await self.courses_repository.get_course_by_code(
                        course_code=course.CourseCode,
                        department_id=department.id
                    )

                    if not course_in_db:
                        raise NotFoundException(detail="Course not found!")

            return await self.repository.save(syllabus=syllabus)

        except ET.ParseError:
            raise HTTPException(status_code=400, detail="Invalid XML format.")

    async def getByDepartmentID(self, department_id) -> Optional[SyllabusParsed]:
        return await self.repository.getByDeptID(department_id)

    async def getByDeptIDAndSemesterCode(self, department_id: int, semester_code: int) -> Optional[SyllabusParsed]:
        return await self.repository.getByDeptIDAndSemesterCode(department_id, semester_code)

    async def updateSyllabus(self, department_id: int, semester_code: int, course_code: str, course_type: str) -> \
            Optional[SyllabusParsed]:
        return await self.repository.updateSyllabus(department_id, semester_code, course_code, course_type)

    async def template(self, department_id: int) -> Optional[Any]:
        semesters = await self.repository.getSemesters(department_id)
        courses = await self.repository.getCourses(department_id)
        template = create_template(department_id, semesters, courses)
        return template
