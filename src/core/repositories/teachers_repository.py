from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.teachers_repository_contract import TeachersRepositoryContract
from src.core.entities.teacher import Teacher
from src.infrastructure.repositories.base_repository import BaseRepository


class TeachersRepository(
    BaseRepository[Teacher], TeachersRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Teacher)
