from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi import status

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services import PreferenceServiceContract
from src.models.preference import PreferenceIn
from src.models.response import APIResponse

preference_router = APIRouter(prefix="/preferences")


@preference_router.post("")
@inject
async def create_preference(
        preference_in: PreferenceIn,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    return await preference_service.create_preference(preference_in)


@preference_router.get("")
@inject
async def get_all_preferences(
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    return await preference_service.get_preferences()


@preference_router.get("/{id}")
@inject
async def get_preference(
        id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    return await preference_service.get_preference_by_id(id)


@preference_router.put("/{id}")
@inject
async def update_preference(
        id: int,
        preference_in: PreferenceIn,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    return await preference_service.update_preference(id, preference_in)


@preference_router.delete("/{id}")
@inject
async def delete_preference(
        id: int,
        preference_service: PreferenceServiceContract = Depends(Provide[AdminContainer.preference_service]),
):
    return await preference_service.delete_preference(id)
