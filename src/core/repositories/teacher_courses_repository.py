from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.entities.teacher_course import TeacherCourse
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
