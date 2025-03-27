from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.exam_routines_repository_contract import ExamRoutinesRepositoryContract
from src.core.entities.exam_routines import ExamRoutine
from src.infrastructure.repositories.base_repository import BaseRepository


class ExamRoutinesRepository(
    BaseRepository[ExamRoutine], ExamRoutinesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, ExamRoutine)