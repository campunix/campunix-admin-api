import json
from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends
from src.features.routine.models.routine_in import RoutineIn
from src.features.routine.routine_container import RoutineContainer
from src.features.routine.services.routine_service_contract import RoutineServiceContract

router = APIRouter()

@router.post("/routine")
@inject
async def generate_routine(
    routine_in: RoutineIn,
    routine_generator: RoutineServiceContract = Depends(Provide[RoutineContainer.routine_service])
):
    response_data = await routine_generator.generate_routine_async(routine_in.total_slots)
    return response_data
