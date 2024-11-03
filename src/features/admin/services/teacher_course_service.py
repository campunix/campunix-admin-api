from typing import Optional

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.entities.teacher_course import TeacherCourse
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.TeacherServiceContract import TeacherServiceContract
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.features.admin.services.teacher_course_service_contract import TeacherCourseCourseServiceContract
from src.models.teacher_course import TeacherCourseOut, TeacherCourseIn


class TeacherCourseService(TeacherCourseCourseServiceContract):
    def __init__(
            self,
            teacher_course_repository: TeacherCoursesRepositoryContract,
            teacher_service: TeacherServiceContract,
            course_service: CourseServiceContract
    ):
        self.teacher_course_repository = teacher_course_repository
        self.teacher_service = teacher_service
        self.course_service = course_service

    async def create_teacher_course(self, teacher_course: TeacherCourseIn) -> Optional[TeacherCourseOut]:
        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)
        course = await self.course_service.get_course_by_id(teacher_course.course_id)

        new_teacher_course = await self.teacher_course_repository.create(
            TeacherCourse(
                teacher_id=teacher.id,
                course_id=course.id
            )
        )
        return TeacherCourseOut(
            id=new_teacher_course.id,
            teacher=teacher,
            course=course
        )

    async def get_teacher_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return self.teacher_course_repository.get_all()

    async def update_teacher_course(self, id: int, teacher_course: TeacherCourseIn) -> Optional[TeacherCourseOut]:
        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)
        course = await self.course_service.get_course_by_id(teacher_course.course_id)

        new_teacher_course = await self.teacher_course_repository.update(
            id,
            TeacherCourse(
                teacher_id=teacher.id,
                course_id=course.id
            )
        )

        return TeacherCourseOut(
            id=new_teacher_course.id,
            teacher=teacher,
            course=course
        )

    async def delete_teacher_course(self, id: int) -> bool:
        return await self.teacher_course_repository.delete(id)

    async def get_teacher_course_by_id(self, id: int) -> Optional[TeacherCourseOut]:
        teacher_course = await self.teacher_course_repository.get_by_id(id)

        if not teacher_course:
            raise NotFoundException(detail="Teachers courses not found!")

        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)
        course = await self.course_service.get_course_by_id(teacher_course.course_id)

        return TeacherCourseOut(
            id=teacher_course.id,
            teacher=teacher,
            course=course
        )
