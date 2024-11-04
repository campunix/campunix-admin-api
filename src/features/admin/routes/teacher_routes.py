from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.TeacherServiceContract import TeacherServiceContract
from src.models.teacher import TeacherIn
from src.utils.oauth2_utils import oauth2_scheme

teacher_router = APIRouter(prefix="/teachers")


@teacher_router.post("")
@inject
async def create_teacher(
        teacher_in: TeacherIn,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
):
    teacher = await teacher_service.create_teacher(teacher_in)
    return teacher


@teacher_router.get("")
@inject
async def get_all_teacher(
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
):
    return await teacher_service.get_teachers()


@teacher_router.get("/{id}")
@inject
async def get_teacher(
        id: int,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
):
    return await teacher_service.get_teacher_by_id(id)


@teacher_router.put("/{id}")
@inject
async def update_teacher(
        id: int,
        teacher_in: TeacherIn,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
):
    teacher = await teacher_service.update_teacher(id, teacher_in)
    return teacher


@teacher_router.delete("/{id}")
@inject
async def delete_teacher(
        id: int,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
):
    status = await teacher_service.delete_teacher(id)
    return status
