from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.departments_repository_contract import DepartmentsRepositoryContract
from src.core.entities.department import Department
from src.infrastructure.repositories.base_repository import BaseRepository


class DepartmentsRepository(
    BaseRepository[Department], DepartmentsRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Department)
