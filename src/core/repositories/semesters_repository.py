from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.semesters_repository_contract import SemestersRepositoryContract
from src.core.entities.semester import Semester
from src.infrastructure.repositories.base_repository import BaseRepository


class SemestersRepository(
    BaseRepository[Semester], SemestersRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Semester)

    async def get_semester_by_year_and_number(self, year: int, number: int) -> Optional[Semester]:
        result = await self.db_session.execute(
            select(Semester).where(Semester.year == year and Semester.number == number))

        return result.scalars().one_or_none()
