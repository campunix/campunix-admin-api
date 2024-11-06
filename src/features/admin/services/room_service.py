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

        return RoomOut(**new_room.__dict__)

    async def get_rooms(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        room_dict = await self.rooms_repository.get_all()
        rooms = room_dict.get("items", [])
        room_out_list = [RoomOut(**room.__dict__) for room in rooms]

        if paginate:
            return {
                "items": room_out_list,
                "current_page": room_dict.get("current_page"),
                "total_pages": room_dict.get("total_pages"),
                "page_size": room_dict.get("page_size"),
                "total_items": room_dict.get("total_items"),
            }
        else:
            return {
                "items": room_out_list,
            }

    async def update_room(self, id: int, room: RoomIn) -> Optional[RoomOut]:
        room = await self.rooms_repository.update(
            id=id,
            obj_data=Room(
                name=room.name,
                code=room.code,
                department_id=room.department_id,
                room_type=RoomType.from_str(room.room_type)
            )
        )
        return RoomOut(**room.__dict__)

    async def delete_room(self, id: int) -> bool:
        return await self.rooms_repository.delete(id)

    async def get_room_by_id(self, id: int) -> Optional[RoomOut]:
        room = await self.rooms_repository.get_by_id(id)
        return RoomOut(**room.__dict__)
