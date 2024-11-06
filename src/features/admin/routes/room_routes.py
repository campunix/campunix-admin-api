from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status
from starlette.status import HTTP_201_CREATED

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.room_service_contract import RoomServiceContract
from src.models.response import APIResponse
from src.models.room import RoomIn

room_router = APIRouter(prefix="/rooms")


@room_router.post("")
@inject
async def create_room(
        room_in: RoomIn,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        # token: str = Depends(oauth2_scheme),
):
    room = await room_service.create_room(room_in)
    return APIResponse(code=HTTP_201_CREATED, message="Created successfully", data=room)


@room_router.get("")
@inject
async def get_all_room(
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    rooms = await room_service.get_rooms()
    return APIResponse(data=rooms)


@room_router.get("/{id}")
@inject
async def get_room(
        id: int,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    room = await room_service.get_room_by_id(id)
    return APIResponse(data=room)


@room_router.put("/{id}")
@inject
async def update_room(
        id: int,
        room_in: RoomIn,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    room = await room_service.update_room(id, room_in)
    return APIResponse(messages="Updated successfully", data=room)


@room_router.delete("/{id}")
@inject
async def delete_room(
        id: int,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
):
    res = await room_service.delete_room(id)
    if res is True:
        return APIResponse(messages="Deleted successfully")
    else:
        return APIResponse(status=res, code=status.HTTP_204_NO_CONTENT, messages="Deletion unsuccessful")
