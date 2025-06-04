import math
from typing import Optional, List

from sqlmodel import or_

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.converters import entity_to_model_list
from src.core.entities.course import Course
from src.core.entities.teacher import Teacher
from src.core.entities.teacher_course import TeacherCourse
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.features.admin.services.teacher_course_service_contract import TeacherCourseServiceContract
from src.features.admin.services.teacher_service_contract import TeacherServiceContract
from src.models.course_teacher_map import CoursesTeachers
from src.models.syllabus.syllabus_models import TeacherCourseOutForSyllabus
from src.models.teacher_course_map import TeachersCourseOut, TeachersCourseIn, TeachersCourseMappingOut


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

    async def create_teacher_course(self, teacher_course: TeachersCourseIn) -> List[TeachersCourseOut]:
        course = await self.course_service.get_course_by_id(teacher_course.course_id)

        if not course:
            raise NotFoundException(detail="Course not found")

        results = []

        for teacher_id in teacher_course.teacher_ids:
            teacher = await self.teacher_service.get_teacher_by_id(teacher_id)

            if not teacher:
                continue

            new_teacher_course = await self.teacher_course_repository.create(
                TeacherCourse(
                    teacher_id=teacher.id,
                    course_id=course.id
                )
            )

            if not new_teacher_course:
                continue

            results.append(
                TeachersCourseOut(
                    id=course.id,
                    title=course.title,
                    code=course.code,
                    course_type=course.course_type,
                    relation_id=new_teacher_course.id
                )
            )

        return results

    async def get_teacher_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                                  search_query: Optional[str] = None, ):

        filters = []
        joins = [(Course, TeacherCourse.course_id == Course.id)]

        if search_query:
            filters.append(
                or_(
                    Course.title.ilike(f"%{search_query}%"),
                    Course.code.ilike(f"%{search_query}%")
                )
            )

        # First, count unique course_ids matching filters
        total_items = await self.teacher_course_repository.count_distinct(
            field=TeacherCourse.course_id,
            filters=filters,
            joins=joins
        )

        course_ids = await self.teacher_course_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters,
            columns=[TeacherCourse.course_id],
            group_by=[TeacherCourse.course_id],
            joins=joins
        )

        teacher_courses = course_ids.get("items", [])

        if not teacher_courses:
            raise NotFoundException(detail="Teachers courses not found!")

        results = []

        # Then get full course details for each course_id
        for tc in teacher_courses:
            course = await self.course_service.get_course_by_id(tc["course_id"])

            # Get all teachers for this course
            teachers = await self.teacher_course_repository.get_all(
                filters=[TeacherCourse.course_id == tc["course_id"]],
                joins=[(Teacher, TeacherCourse.teacher_id == Teacher.id)]
            )

            results.append({
                "id": tc["course_id"],
                "course": course,
                "teachers": teachers["items"] if teachers else []
            })

        # Pagination metadata
        total_pages = math.ceil(total_items / page_size)

        # Prepare response data
        data = {
            "current_page": page,
            "items": results,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages
        }

        return entity_to_model_list(entity_dict=data, model=TeachersCourseMappingOut, paginate=paginate)

    async def update_teacher_course(self, id: int, teacher_course: TeachersCourseIn) -> Optional[TeachersCourseOut]:
        res = await self.delete_teacher_course(teacher_course.course_id)

        if not res:
            raise NotFoundException(detail='Course not found')

        return await self.create_teacher_course(teacher_course)

    async def delete_teacher_course(self, id: int) -> bool:
        res = await self.teacher_course_repository.delete_by_course_id(id)
        if res is False:
            raise NotFoundException(detail="Deletion unsuccessful")
        return res

    async def get_teacher_course_by_id(self, course_id: int) -> Optional[CoursesTeachers]:
        course = await self.course_service.get_course_by_id(course_id)
        teachers = await self.teacher_course_repository.get_teachers_by_course(course_id=course.id)

        if not teachers:
            raise NotFoundException(detail="Teachers not found!")

        if not course:
            raise NotFoundException(detail="Course not found!")

        teacher_ids = [item['teacher'].id for item in teachers]
        department_id = teachers[0]['department'].id

        return CoursesTeachers(
            course_id=course.id,
            title=course.title,
            code=course.code,
            teachers=teacher_ids,
            department_id=department_id
        )

    async def get_teacher_course_by_course_code(self, department_id: int, course_code: str) -> Optional[
        TeacherCourseOutForSyllabus]:
        course = await self.course_service.get_course_by_course_code(
            department_id=department_id,
            course_code=course_code
        )

        teacher_course = await self.teacher_course_repository.get_teacher_courses_by_course_id(course_id=course.id)

        if not teacher_course:
            raise NotFoundException(detail="Course teacher not found!")

        teacher = await self.teacher_service.get_teacher_by_id(teacher_course.teacher_id)

        return TeacherCourseOutForSyllabus(
            id=teacher_course.id,
            teacher=teacher,
            course=course
        )
