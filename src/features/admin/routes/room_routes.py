from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.room_service_contract import RoomServiceContract
from src.models.room import RoomIn
from src.utils.oauth2_utils import oauth2_scheme

room_router = APIRouter(prefix="/rooms")


@room_router.post("")
@inject
async def create_room(
        room_in: RoomIn,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        token: str = Depends(oauth2_scheme),
):
    room = await room_service.create_room(room_in)
    return room


@room_router.get("")
@inject
async def get_all_room(
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    return await room_service.get_rooms()


@room_router.get("/{id}")
@inject
async def get_room(
        id: int,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    return await room_service.get_room_by_id(id)


@room_router.put("/{id}")
@inject
async def update_room(
        id: int,
        room_in: RoomIn,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    room = await room_service.update_room(id, room_in)
    return room


@room_router.delete("/{id}")
@inject
async def delete_room(
        id: int,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    room = await room_service.delete_room(id)
    return room
