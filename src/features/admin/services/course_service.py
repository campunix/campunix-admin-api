from typing import Optional, List

from sqlmodel import select

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.entities.course import Course
from src.core.entities.enums.course_type import CourseType
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.models.course import CourseOut, CourseIn


class CourseService(CourseServiceContract):
    def __init__(
            self,
            course_repository: CoursesRepositoryContract,
    ):
        self.course_repository = course_repository

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

    async def get_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.course_repository.get_all()

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
        return CourseOut(
            id=course.id,
            title=course.title,
            code=course.code,
            course_type=course.course_type.value
        )

    async def get_course_by_course_code(self, department_id: int, course_code: str) -> Optional[CourseOut]:
        course = await self.course_repository.get_course_by_code(course_code=course_code, department_id=department_id)
        return CourseOut(
            id=course.id,
            title=course.title,
            code=course.code,
            course_type=course.course_type.value
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
