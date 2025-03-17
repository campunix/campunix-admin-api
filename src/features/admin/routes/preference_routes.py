from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.admin_container import AdminContainer
from src.features.admin.services import PreferenceServiceContract
from src.models.preference import PreferenceIn
from src.models.response import APIResponse, UpdateResponse, DeleteResponse, CreateResponse

preference_router = APIRouter(prefix="/preferences")


@preference_router.get("/days")
@inject
async def days(
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    types = await preference_service.get_days()
    return APIResponse(data=types)


@preference_router.post("")
@inject
async def create_preference(
        preference_in: PreferenceIn,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    preference = await preference_service.create_preference(preference_in)
    return CreateResponse(data=preference)


@preference_router.get("")
@inject
async def get_all_preferences(
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    preferences = await preference_service.get_preferences()
    return APIResponse(data=preferences)


@preference_router.get("/{id}")
@inject
async def get_preference(
        id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
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
):
    preference = await preference_service.update_preference(id, preference_in)

    if not preference:
        raise NotFoundException

    return UpdateResponse(data=preference)


@preference_router.delete("/{id}")
@inject
async def delete_preference(
        id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    is_deleted = await preference_service.delete_preference(id)

    if not is_deleted:
        raise NotFoundException

    return DeleteResponse()
