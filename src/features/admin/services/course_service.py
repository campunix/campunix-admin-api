from typing import Optional, List, Dict, Any

from sqlmodel import select

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.converters import entity_to_model_list
from src.core.entities.course import Course
from src.core.entities.enums.course_type import CourseType
from src.core.exceptions.not_found_exception import NotFoundException
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
        courses = await self.course_repository.get_all(page=page, page_size=page_size, paginate=paginate)
        return entity_to_model_list(entity_dict=courses, model=CourseOut, paginate=paginate)

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


    async def get_course_types(self) -> Dict[str, Any]:
        course_types = await self.course_repository.get_course_types()

        if not course_types:
            raise NotFoundException()

        return course_types
