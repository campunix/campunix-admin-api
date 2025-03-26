from typing import Optional, List, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.entities.course import Course
from src.core.entities.department import Department
from src.core.entities.teacher import Teacher
from src.core.entities.teacher_course import TeacherCourse
from src.core.entities.user import User
from src.infrastructure.repositories.base_repository import BaseRepository


class TeacherCoursesRepository(
    BaseRepository[TeacherCourse], TeacherCoursesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, TeacherCourse)

    async def get_teacher_courses_by_course_id(self, course_id: int) -> Optional[TeacherCourse]:
        statement = select(TeacherCourse).where(TeacherCourse.course_id == course_id)
        result = await self.db_session.execute(statement)
        return result.scalar_one_or_none()

    async def get_teacher_courses_by_teacher_id(self, teacher_id: int) -> Optional[TeacherCourse]:
        statement = select(TeacherCourse).where(TeacherCourse.teacher_id == teacher_id)
        result = await self.db_session.execute(statement)
        return result.scalar_one_or_none()

    async def get_all_teacher_courses_by_course_id(self, course_id: int) -> Optional[List[Dict[str, Any]]]:
        statement = (
            select(
                TeacherCourse,
                Teacher,
                User,
                Department
            )
            .where(TeacherCourse.course_id == course_id)
            .join(Teacher, Teacher.id == TeacherCourse.teacher_id)
            .join(User, Teacher.user_id == User.id)
            .join(Department, Teacher.department_id == Department.id)
        )
        results = await self.db_session.execute(statement)

        outputs = []
        for teacher_course, teacher, user, department in results:
            item = {
                "teacher_course": teacher_course,
                "teacher": teacher,
                "user": user,
                "department": department
            }

            outputs.append(item)
            pass

        return outputs
