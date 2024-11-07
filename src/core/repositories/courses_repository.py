from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.entities.course import Course
from src.infrastructure.repositories.base_repository import BaseRepository


class CoursesRepository(
    BaseRepository[Course], CoursesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Course)

    async def get_course_by_code(self, course_code: str, department_id: int) -> Optional[Course]:
        result = await self.db_session.execute(
            select(Course).where(Course.code == course_code and Course.department_id == department_id))

        return result.scalars().one_or_none()
