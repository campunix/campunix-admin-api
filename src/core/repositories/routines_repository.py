from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.contracts.routines_repository_contract import RoutinesRepositoryContract
from src.core.entities.routine import Routine
from src.infrastructure.repositories.base_repository import BaseRepository


class RoutinesRepository(
    BaseRepository[Routine], RoutinesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Routine)