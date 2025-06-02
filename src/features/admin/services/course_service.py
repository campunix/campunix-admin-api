from typing import Optional, List, Dict, Any

from sqlmodel import and_
from sqlmodel import or_

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.converters import entity_to_model_list
from src.core.entities.course import Course
from src.core.entities.department import Department
from src.core.entities.enums.course_type import CourseType
from src.core.entities.teacher import Teacher
from src.core.entities.teacher_course import TeacherCourse
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.models.course import CourseOut, CourseIn
from src.models.course_teacher_map import CoursesTeacherOut
from src.models.department import DepartmentOut


class CourseService(CourseServiceContract):
    def __init__(
            self,
            course_repository: CoursesRepositoryContract,
            teacher_course_repository: TeacherCoursesRepositoryContract
    ):
        self.course_repository = course_repository
        self.teacher_course_repository = teacher_course_repository

    async def create_course(self, course: CourseIn) -> Optional[CourseOut]:
        course_type = CourseType.from_str(course.course_type)

        new_course = await self.course_repository.create(
            Course(
                title=course.title,
                code=course.code,
                department_id=course.department_id,
                course_type=course_type
            )
        )

        return CourseOut(
            id=new_course.id,
            title=new_course.title,
            code=new_course.code,
            course_type=new_course.course_type.value
        )

    async def get_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                          search_query: Optional[str] = None, department_id: Optional[int] = None):

        filters = []

        if search_query:
            filters.append(
                or_(
                    Course.title.ilike(f"%{search_query}%"),
                    Course.code.ilike(f"%{search_query}%")
                )
            )

        if department_id:
            filters.append(
                and_(
                    Course.department_id == department_id
                )
            )

        courses = await self.course_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters
        )

        updated_items = []
        for course in courses["items"]:
            courses_dict_item = dict(course)
            teachers = await self.get_teachers_by_course(course_id=courses_dict_item["id"])
            if teachers:
                courses_dict_item["course_teachers"] = teachers

            updated_items.append(courses_dict_item)

        courses["items"] = updated_items

        return entity_to_model_list(entity_dict=courses, model=CourseOut, paginate=paginate)

    async def get_courses_by_teacher_id(self, teacher_id: int, page: int = 1, page_size: int = 10,
                                        paginate: bool = False,
                                        search_query: Optional[str] = None):

        filters = []

        if teacher_id:
            filters.append(Teacher.id == teacher_id)

        if search_query:
            filters.append(
                or_(
                    Course.title.ilike(f"%{search_query}%"),
                    Course.code.ilike(f"%{search_query}%")
                )
            )

        columns = [
            Course.id,
            Course.title,
            Course.code,
            Course.course_type
        ]

        course_dict = await self.course_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters,
            joins=[(TeacherCourse, TeacherCourse.course_id == Course.id)],
            columns=columns,
            group_by=[Course.id]
        )
        return entity_to_model_list(entity_dict=course_dict, model=CourseOut, paginate=paginate)

    async def update_course(self, id: int, course: CourseIn) -> Optional[CourseOut]:
        course_type = CourseType.from_str(course.course_type)

        new_course = await self.course_repository.update(
            id,
            Course(
                title=course.title,
                code=course.code,
                department_id=course.department_id,
                course_type=course_type
            )
        )

        if not new_course:
            raise NotFoundException

        return CourseOut(
            id=new_course.id,
            title=new_course.title,
            code=new_course.code,
            course_type=new_course.course_type.value
        )

    async def delete_course(self, id: int) -> bool:
        return await self.course_repository.delete(id)

    async def get_course_by_id(self, id: int) -> Optional[CourseOut]:
        course = await self.course_repository.get_by_id(id)

        if not course:
            raise NotFoundException

        course_teachers = await self.get_teachers_by_course(id)
        return CourseOut(
            id=course.id,
            title=course.title,
            code=course.code,
            course_type=course.course_type.value,
            course_teachers=course_teachers
        )

    async def get_course_by_course_code(self, department_id: int, course_code: str) -> Optional[CourseOut]:
        course = await self.course_repository.get_course_by_code(course_code=course_code, department_id=department_id)

        if not course:
            raise NotFoundException

        course_teachers = await self.get_teachers_by_course(course.id)

        return CourseOut(
            id=course.id,
            title=course.title,
            code=course.code,
            course_type=course.course_type.value,
            course_teachers=course_teachers
        )

    async def bulk_insert_courses(self, courses_in: List[CourseIn]):
        courses = [
            Course(
                title=course.title,
                code=course.code,
                department_id=course.department_id,
                course_type=CourseType.from_str(course.course_type)
            ) for course in courses_in
        ]

        await self.course_repository.bulk_insert(courses)

    async def get_course_types(self) -> Dict[str, Any]:
        course_types = await self.course_repository.get_course_types()

        if not course_types:
            raise NotFoundException()

        return course_types

    async def get_teachers_by_course(self, course_id: int) -> Optional[List[CoursesTeacherOut]]:
        teacher_courses = await self.teacher_course_repository.get_teachers_by_course(course_id=course_id)
        course_teachers = []

        for teacher_course in teacher_courses:
            teacher_course_row = teacher_course["teacher_course"]
            teacher = teacher_course["teacher"]
            user = teacher_course["user"]
            department = teacher_course["department"]
            course_teachers.append(
                CoursesTeacherOut(
                    id=teacher.id,
                    full_name=user.full_name,
                    email=user.email,
                    designation=teacher.designation,
                    status=teacher.status,
                    department=DepartmentOut(id=department.id, name=department.name, code=department.code),
                    relation_id=teacher_course_row.id
                )
            )

        return course_teachers
