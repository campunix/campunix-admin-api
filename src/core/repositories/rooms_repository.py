from typing import Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.rooms_repository_contract import RoomsRepositoryContract
from src.core.entities.enums.room_type import RoomType
from src.core.entities.room import Room
from src.infrastructure.repositories.base_repository import BaseRepository


class RoomsRepository(
    BaseRepository[Room], RoomsRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Room)

    async def get_room_types(self) -> Dict[str, Any]:
        # room_types = {room_type.name: room_type.value for room_type in RoomType}
        return {"roomTypes": [room.value for room in RoomType]}
