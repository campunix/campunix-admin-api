from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.departments_repository_contract import DepartmentsRepositoryContract
from src.core.entities.department import Department
from src.infrastructure.repositories.base_repository import BaseRepository


class DepartmentsRepository(
    BaseRepository[Department], DepartmentsRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Department)

    async def get_department_by_code(self, department_code: str) -> Optional[Department]:
        result = await self.db_session.execute(select(Department).where(Department.code == department_code))

        return result.scalars().one_or_none()
