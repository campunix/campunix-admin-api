from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.rooms_repository_contract import RoomsRepositoryContract
from src.core.entities.room import Room
from src.infrastructure.repositories.base_repository import BaseRepository


class RoomsRepository(
    BaseRepository[Room], RoomsRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Room)
