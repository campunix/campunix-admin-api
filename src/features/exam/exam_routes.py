from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.exam.exam_container import ExamContainer
from src.features.exam.services.exam_routine_service_contract import ExamRoutineServiceContract
from src.models.exam_routine import ExamRoutineIn
from src.models.response import CreateResponse, APIResponse, UpdateResponse, DeleteResponse

exam_routine_router = APIRouter(prefix="/examRoutines")

@exam_routine_router.post("")
@inject
async def save_exam_routine(
        exam_routine_in: ExamRoutineIn,
        exam_routine_service: ExamRoutineServiceContract = Depends(Provide[ExamContainer.exam_routine_service]),
):
    data = await exam_routine_service.save_exam_routine(exam_routine_in=exam_routine_in)

    return CreateResponse(data=data)


@exam_routine_router.get("")
@inject
async def get_all_exam_routines(
        exam_routine_service: ExamRoutineServiceContract = Depends(Provide[ExamContainer.exam_routine_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None
):
    routines = await exam_routine_service.get_exam_routines(page=page, page_size=page_size, search_query=search_query,
                                                        paginate=True)
    return APIResponse(data=routines)


@exam_routine_router.get("/{id}")
@inject
async def get_exam_routine(
        id: int,
        exam_routine_service: ExamRoutineServiceContract = Depends(Provide[ExamContainer.exam_routine_service]),
):
    routine = await exam_routine_service.get_exam_routine_by_id(id=id)

    return APIResponse(data=routine)


@exam_routine_router.put("/{id}")
@inject
async def update_exam_routines(
        id: int,
        exam_routine_in: ExamRoutineIn,
        exam_routine_service: ExamRoutineServiceContract = Depends(Provide[ExamContainer.exam_routine_service]),
):
    updated_routine = await exam_routine_service.update_exam_routine(id=id, exam_routine_in=exam_routine_in)

    return UpdateResponse(data=updated_routine)


@exam_routine_router.delete("/{id}")
@inject
async def delete_exam_routine(
        id: int,
        exam_routine_service: ExamRoutineServiceContract = Depends(Provide[ExamContainer.exam_routine_service]),
):
    await exam_routine_service.delete_exam_routine(id)

    return DeleteResponse(message="Routine deleted!")