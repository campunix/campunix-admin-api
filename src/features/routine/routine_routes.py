from dependency_injector.wiring import inject

from fastapi import APIRouter, HTTPException
from src.core.exceptions.duplicate_exception import DuplicateException
from src.features.routine.models.routine_in import RoutineIn
from src.features.routine.routine_generator import RoutineGenerator

router = APIRouter()

@router.post("/routine")
@inject
async def generate_routine(routine_in: RoutineIn):
    routine_generator = RoutineGenerator()
    return routine_generator.generate(
        total_slots=routine_in.total_slots)
