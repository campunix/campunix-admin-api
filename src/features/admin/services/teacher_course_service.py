from typing import Optional

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.converters import entity_to_model_list
from src.core.entities.course import Course
from src.core.entities.teacher import Teacher
from src.core.entities.teacher_course import TeacherCourse
from src.core.entities.user import User
from src.core.exceptions.duplicate_exception import DuplicateException
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.TeacherServiceContract import TeacherServiceContract
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.features.admin.services.teacher_course_service_contract import TeacherCourseServiceContract
from src.models.teacher_course import TeacherCourseOut, TeacherCourseIn


class TeacherCourseService(TeacherCourseServiceContract):
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

        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        if not course:
            raise NotFoundException(detail="Course not found")

        new_teacher_course = await self.teacher_course_repository.create(
            TeacherCourse(
                teacher_id=teacher.id,
                course_id=course.id
            )
        )

        if not new_teacher_course:
            raise DuplicateException(detail="Teacher Course already exist")

        return TeacherCourseOut(
            id=new_teacher_course.id,
            teacher=teacher,
            course=course
        )

    async def get_teacher_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        columns = [
            TeacherCourse.id,
            Teacher.id.label("teacherId"),
            User.full_name,
            User.email,
            Teacher.designation,
            Teacher.status,
            Course.id.label("courseId"),
            Course.title,
            Course.code,
            Course.course_type
        ]

        teacher_course_dict = await self.teacher_course_repository.get_all(
            joins=[
                (Teacher, TeacherCourse.teacher_id == Teacher.id),
                (User, Teacher.user_id == User.id),
                (Course, TeacherCourse.course_id == Course.id)],
            columns=columns
        )
        return entity_to_model_list(entity_dict=teacher_course_dict, model=TeacherCourseOut, paginate=paginate)

    async def update_teacher_course(self, id: int, teacher_course: TeacherCourseIn) -> Optional[TeacherCourseOut]:
        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)
        course = await self.course_service.get_course_by_id(teacher_course.course_id)

        if not teacher:
            raise NotFoundException(detail='Teacher not found')

        if not course:
            raise NotFoundException(detail='Course not found')

        new_teacher_course = await self.teacher_course_repository.update(
            id,
            TeacherCourse(
                teacher_id=teacher.id,
                course_id=course.id
            )
        )

        if not new_teacher_course:
            raise NotFoundException(detail='Teacher Course not found')

        return TeacherCourseOut(
            id=new_teacher_course.id,
            teacher=teacher,
            course=course
        )

    async def delete_teacher_course(self, id: int) -> bool:
        res = await self.teacher_course_repository.delete(id)
        if res is False:
            raise NotFoundException(detail="Deletion unsuccessful")
        return res

    async def get_teacher_course_by_id(self, id: int) -> Optional[TeacherCourseOut]:
        teacher_course = await self.teacher_course_repository.get_by_id(id)

        if not teacher_course:
            raise NotFoundException(detail="Teachers courses not found!")

        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)
        course = await self.course_service.get_course_by_id(teacher_course.course_id)

        if not teacher:
            raise NotFoundException(detail="Teacher not found!")

        if not course:
            raise NotFoundException(detail="Course not found!")

        return TeacherCourseOut(
            id=teacher_course.id,
            teacher=teacher,
            course=course
        )
