from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.routine.models.routine_in import RoutineIn, SavedRoutineIn
from src.features.routine.routine_container import RoutineContainer
from src.features.routine.services.routine_contract import RoutineServiceContract
from src.models.response import CreateResponse, DeleteResponse, APIResponse, UpdateResponse

routine_router = APIRouter(prefix="/routines")


@routine_router.post("/generate")
@inject
async def generate_routine(
        routine_in: RoutineIn,
        routine_generator: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service])
):
    response_data = await routine_generator.generate_routine_async(
        routine_in.syllabus_id,
        routine_in.total_slots)
    return response_data


@routine_router.post("")
@inject
async def save_routine_in_db(
        routine_in: SavedRoutineIn,
        routine_service: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service]),
):
    data = await routine_service.save_routine(routine_save_in=routine_in)

    return CreateResponse(data=data)


@routine_router.get("")
@inject
async def get_all_routines_from_db(
        routine_service: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None
):
    routines = await routine_service.get_saved_routines(page=page, page_size=page_size, search_query=search_query,
                                                        paginate=True)
    return APIResponse(data=routines)


@routine_router.get("/{id}")
@inject
async def get_routine_from_db(
        id: int,
        routine_service: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service]),
):
    routine = await routine_service.get_routine_by_id(id=id)

    return APIResponse(data=routine)


@routine_router.put("/{id}")
@inject
async def update_routine_in_db(
        id: int,
        routine_in: SavedRoutineIn,
        routine_service: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service]),
):
    updated_routine = await routine_service.update_saved_routine(id=id, routine_save_in=routine_in)

    return UpdateResponse(data=updated_routine)


@routine_router.delete("/{id}")
@inject
async def delete_routine_form_db(
        id: int,
        routine_service: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service]),
):
    await routine_service.delete_routine(id)

    return DeleteResponse(message="Routine deleted!")
