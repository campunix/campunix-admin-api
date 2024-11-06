from typing import Optional

from src.core.contracts.rooms_repository_contract import RoomsRepositoryContract
from src.core.entities.enums.room_type import RoomType
from src.core.entities.room import Room
from src.features.admin.services.room_service_contract import RoomServiceContract
from src.models.room import RoomOut, RoomIn


class RoomService(RoomServiceContract):
    def __init__(
            self,
            rooms_repository: RoomsRepositoryContract,
    ):
        self.rooms_repository = rooms_repository

    async def create_room(self, room: RoomIn) -> Optional[RoomOut]:
        new_room = await self.rooms_repository.create(
            Room(
                name=room.name,
                code=room.code,
                department_id=room.department_id,
                room_type=RoomType.from_str(room.room_type)
            )
        )

        return RoomOut(
            id=new_room.id,
            name=new_room.name,
            code=new_room.code,
            room_type=new_room.room_type.value
        )

    async def get_rooms(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.rooms_repository.get_all()

    async def update_room(self, id: int, room: RoomIn) -> Optional[RoomOut]:
        return await self.rooms_repository.update(
            id=id,
            obj_data=Room(
                name=room.name,
                code=room.code,
                department_id=room.department_id,
                room_type=RoomType.from_str(room.room_type)
            )
        )

    async def delete_room(self, id: int) -> bool:
        return await self.rooms_repository.delete(id)

    async def get_room_by_id(self, id: int) -> Optional[RoomOut]:
        return await self.rooms_repository.get_by_id(id)
