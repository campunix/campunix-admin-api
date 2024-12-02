from typing import Optional

from src.core.contracts.rooms_repository_contract import RoomsRepositoryContract
from src.core.converters import entity_to_model, entity_to_model_list
from src.core.entities.enums.room_type import RoomType
from src.core.entities.room import Room
from src.core.exceptions.not_found_exception import NotFoundException
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

        return entity_to_model(entity=new_room, model=RoomOut)

    async def get_rooms(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        data = await self.rooms_repository.get_all()
        rooms = {
            "rooms": [
                {key: value for key, value in item.items() if
                 key not in ["created_at", "updated_at"]}
                for item in data["items"]
            ]
        }

        return rooms

    async def update_room(self, id: int, roomIn: RoomIn) -> Optional[RoomOut]:
        room = await self.rooms_repository.update(
            id=id,
            obj_data=Room(
                name=roomIn.name,
                code=roomIn.code,
                department_id=roomIn.department_id,
                room_type=RoomType.from_str(roomIn.room_type)
            )
        )

        if room is None:
            raise NotFoundException(detail='Room not found')

        return entity_to_model(entity=room, model=RoomOut)

    async def delete_room(self, id: int) -> bool:
        res = await self.rooms_repository.delete(id)

        if res is False:
            raise NotFoundException(detail="Deletion unsuccessful")

        return res

    async def get_room_by_id(self, id: int) -> Optional[RoomOut]:
        room = await self.rooms_repository.get_by_id(id)
        return entity_to_model(entity=room, model=RoomOut)

    async def get_room_types(self):
        return await self.rooms_repository.get_room_types()
