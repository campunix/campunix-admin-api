from dependency_injector.wiring import inject

from fastapi import APIRouter, HTTPException
from src.core.exceptions.duplicate_exception import DuplicateException
from src.features.routine.routine_generator import RoutineGenerator

router = APIRouter()

@router.get("/routine")
@inject
async def generate_routine():
    #raise HTTPException(500, "This is an error")
    # raise DuplicateException("This is a custom error")
    routine_generator = RoutineGenerator()
    return routine_generator.generate()
