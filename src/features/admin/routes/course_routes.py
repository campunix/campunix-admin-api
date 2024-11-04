from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.course import CourseIn
from src.utils.oauth2_utils import oauth2_scheme

course_router = APIRouter(prefix="/courses")

@course_router.post("")
@inject
async def create_course(
        course: CourseIn,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
):
    return await course_service.create_course(course)


@course_router.get("")
@inject
async def get_all_courses(
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
):
    return await course_service.get_courses()


@course_router.get("/{id}")
@inject
async def get_course(
        id: int,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
):
    return await course_service.get_course_by_id(id)


@course_router.put("/{id}")
@inject
async def update_course(
        id: int,
        course: CourseIn,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
):
    return await course_service.update_course(id, course)


@course_router.delete("/{id}")
@inject
async def delete_course(
        id: int,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
):
    return await course_service.delete_course(id)


