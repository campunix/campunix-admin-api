from typing import Optional, List

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

    async def get_semester_by_year_and_number(self, department: int, year: int, number: int) -> Optional[Semester]:
        query = select(Semester).where(
            (Semester.department_id == department) &
            (Semester.year == year) &
            (Semester.number == number)
        )
        result = await self.db_session.execute(query)

        return result.scalar_one_or_none()

    async def get_semesters_by_department_id(self, department: int) -> Optional[List[Semester]]:
        query = select(Semester).where(Semester.department_id == department)
        result = await self.db_session.execute(query)

        return list(result.scalars())
