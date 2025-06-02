from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.admin_container import AdminContainer
from src.features.admin.services import PreferenceServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.preference import PreferenceIn
from src.models.response import APIResponse, UpdateResponse, DeleteResponse, CreateResponse
from src.utils.oauth2_utils import oauth2_scheme

preference_router = APIRouter(prefix="/preferences")


@preference_router.get("/days")
@inject
async def days(
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    types = await preference_service.get_days()
    return APIResponse(data=types)


@preference_router.post("")
@inject
async def create_preference(
        preference_in: PreferenceIn,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    preference = await preference_service.create_preference(preference_in)
    return CreateResponse(data=preference)


@preference_router.get("")
@inject
async def get_all_preferences(
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None,
        paginate: bool = True,
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    preferences = await preference_service.get_preferences(page=page, page_size=page_size, paginate=paginate, search_query=search_query,)
    return APIResponse(data=preferences)

@preference_router.get("/byTeacher")
@inject
async def get_preferences_by_teacher_id(
        teacher_id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None,
        paginate: bool = True,
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    preferences = await preference_service.get_preferences_by_teacher_id(page=page, teacher_id=teacher_id, page_size=page_size, paginate=paginate, search_query=search_query,)
    return APIResponse(data=preferences)


@preference_router.get("/{id}")
@inject
async def get_preference(
        id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    preference = await preference_service.get_preference_by_id(id)

    if not preference:
        raise NotFoundException

    return APIResponse(data=preference)


@preference_router.put("/{id}")
@inject
async def update_preference(
        id: int,
        preference_in: PreferenceIn,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    preference = await preference_service.update_preference(id, preference_in)

    if not preference:
        raise NotFoundException

    return UpdateResponse(data=preference)


@preference_router.delete("/{id}")
@inject
async def delete_preference(
        id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    is_deleted = await preference_service.delete_preference(id)

    if not is_deleted:
        raise NotFoundException

    return DeleteResponse()
