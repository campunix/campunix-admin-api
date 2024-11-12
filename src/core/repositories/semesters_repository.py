from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.semesters_repository_contract import SemestersRepositoryContract
from src.core.entities.semester import Semester
from src.infrastructure.repositories.base_repository import BaseRepository


class SemestersRepository(
    BaseRepository[Semester], SemestersRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Semester)
