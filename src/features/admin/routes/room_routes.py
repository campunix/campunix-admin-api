from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.room_service_contract import RoomServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.response import APIResponse, UpdateResponse, CreateResponse
from src.models.room import RoomIn
from src.utils.oauth2_utils import oauth2_scheme

room_router = APIRouter(prefix="/rooms")


@room_router.get("/roomTypes")
@inject
async def room_types(
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    types = await room_service.get_room_types()
    return APIResponse(data=types)


@room_router.post("")
@inject
async def create_room(
        room_in: RoomIn,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    room = await room_service.create_room(room_in)
    return CreateResponse(data=room)


@room_router.get("")
@inject
async def get_all_room(
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None,
        department_id: Optional[int] = None,
        paginate: bool = True,
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    rooms = await room_service.get_rooms(page=page, page_size=page_size, paginate=paginate,
                                         search_query=search_query, department_id=department_id)
    return APIResponse(data=rooms)


@room_router.get("/{id}")
@inject
async def get_room(
        id: int,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    room = await room_service.get_room_by_id(id)
    return APIResponse(data=room)


@room_router.put("/{id}")
@inject
async def update_room(
        id: int,
        room_in: RoomIn,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    room = await room_service.update_room(id, room_in)
    return UpdateResponse(data=room)


@room_router.delete("/{id}")
@inject
async def delete_room(
        id: int,
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    res = await room_service.delete_room(id)
    return APIResponse(status=res, message="Deleted successfully")
