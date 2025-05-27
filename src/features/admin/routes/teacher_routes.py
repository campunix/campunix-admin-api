from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.teacher_service_contract import TeacherServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.response import APIResponse, UpdateResponse, CreateResponse
from src.models.teacher import TeacherIn
from src.utils.oauth2_utils import oauth2_scheme

teacher_router = APIRouter(prefix="/teachers")


@teacher_router.get("/teacherDesignations")
@inject
async def teacher_designation(
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    types = await teacher_service.get_teacher_designation()
    return APIResponse(data=types)


@teacher_router.get("/teacherStatus")
@inject
async def teacher_status(
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    types = await teacher_service.get_teacher_status()
    return APIResponse(data=types)


@teacher_router.post("")
@inject
async def create_teacher(
        teacher_in: TeacherIn,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    teacher = await teacher_service.create_teacher(teacher_in)
    return CreateResponse(data=teacher)


@teacher_router.get("")
@inject
async def get_all_teacher(
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
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

    teachers = await teacher_service.get_teachers(page=page, page_size=page_size, paginate=paginate,
                                                  search_query=search_query, department_id=department_id)
    return APIResponse(data=teachers)


@teacher_router.get("/{id}")
@inject
async def get_teacher(
        id: int,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    teacher = await teacher_service.get_teacher_by_id(id)
    return APIResponse(data=teacher)


@teacher_router.put("/{id}")
@inject
async def update_teacher(
        id: int,
        teacher_in: TeacherIn,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    teacher = await teacher_service.update_teacher(id, teacher_in)
    return UpdateResponse(data=teacher)


@teacher_router.delete("/{id}")
@inject
async def delete_teacher(
        id: int,
        teacher_service: TeacherServiceContract = Depends(Provide[AdminContainer.teacher_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    res = await teacher_service.delete_teacher(id)
    return APIResponse(status=res, message="Deleted successfully")
