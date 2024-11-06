from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from src.models.room import RoomIn, RoomOut


class RoomServiceContract(ABC):
    @abstractmethod
    async def create_room(self, room: RoomIn) -> Optional[RoomOut]:
        pass

    @abstractmethod
    async def get_rooms(self, page: int = 1, page_size: int = 10, paginate: bool = False) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_room(self, id: int, room: RoomIn) -> Optional[RoomOut]:
        pass

    @abstractmethod
    async def delete_room(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_room_by_id(self, id: int) -> Optional[RoomOut]:
        pass
