from typing import Optional, List

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.converters import entity_to_model_list
from src.core.entities.course import Course
from src.core.entities.teacher import Teacher
from src.core.entities.teacher_course import TeacherCourse
from src.core.entities.user import User
from src.core.exceptions.duplicate_exception import DuplicateException
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.teacher_service_contract import TeacherServiceContract
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.features.admin.services.teacher_course_service_contract import TeacherCourseServiceContract
from src.models.course import CourseOut
from src.models.course_teacher_map import CoursesTeacherOut
from src.models.teacher import TeacherOut
from src.models.teacher_course import TeacherCourseIn, TeacherCourseOut
from src.models.teacher_course_map import TeachersCourseOut


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

    async def get_teacher_course_by_course_code(self, department_id: int, course_code: str) -> Optional[
        TeacherCourseOut]:
        course = await self.course_service.get_course_by_course_code(
            department_id=department_id,
            course_code=course_code
        )

        teacher_course = await self.teacher_course_repository.get_teacher_courses_by_course_id(course_id=course.id)

        if not teacher_course:
            raise NotFoundException(detail="Course teacher not found!")

        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)

        return TeacherCourseOut(
            id=teacher_course.id,
            teacher=teacher,
            course=course
        )

    async def assign_teachers(self, course_id: int, teachers: List[int]) -> Optional[CourseOut]:
        course = await self.course_service.get_course_by_id(course_id)

        for teacher_id in teachers:
            teacher_course = await self.create_teacher_course(
                TeacherCourseIn(
                    teacher_id=teacher_id,
                    course_id=course_id
                )
            )

            course.course_teachers.append(
                CoursesTeacherOut(
                    id=teacher_course.teacher.id,
                    full_name=teacher_course.teacher.full_name,
                    email=teacher_course.teacher.email,
                    designation=teacher_course.teacher.designation,
                    status=teacher_course.teacher.status,
                    department=teacher_course.teacher.department
                )
            )

        return course

    async def assign_courses(self, teacher_id: int, courses: List[int]) -> Optional[TeacherOut]:
        teacher = await self.teacher_service.get_teacher_by_id(teacher_id)

        for course_id in courses:
            teacher_course = await self.create_teacher_course(
                TeacherCourseIn(
                    teacher_id=teacher_id,
                    course_id=course_id
                )
            )

            teacher.courses.append(
                TeachersCourseOut(
                    id=teacher_course.course.id,
                    title=teacher_course.course.title,
                    code=teacher_course.course.code,
                    course_type=teacher_course.course.course_type
                )
            )

        return teacher
