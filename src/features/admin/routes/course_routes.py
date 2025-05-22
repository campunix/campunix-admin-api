from typing import List, Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.course_service_contract import CourseServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.course import CourseIn
from src.models.response import CreateResponse, APIResponse, UpdateResponse, DeleteResponse
from src.utils.oauth2_utils import oauth2_scheme

course_router = APIRouter(prefix="/courses")


@course_router.get("/courseTypes")
@inject
async def course_types(
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    types = await course_service.get_course_types()
    return APIResponse(data=types)


@course_router.post("")
@inject
async def create_course(
        course: CourseIn,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    course = await course_service.create_course(course)
    return CreateResponse(data=course)


@course_router.get("")
@inject
async def get_all_courses(
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
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

    courses = await course_service.get_courses(page=page, page_size=page_size, paginate=paginate,
                                               search_query=search_query,
                                               department_id=department_id)
    return APIResponse(data=courses)


@course_router.get("/byTeacher")
@inject
async def get_courses_by_teacher_id(
        teacher_id: int,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None,
        paginate: bool = True,
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    courses = await course_service.get_courses_by_teacher_id(teacher_id=teacher_id, page=page, page_size=page_size,
                                                             paginate=paginate, search_query=search_query)
    return APIResponse(data=courses)


@course_router.get("/{id}")
@inject
async def get_course(
        id: int,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    course = await course_service.get_course_by_id(id)

    if not course:
        raise NotFoundException

    return APIResponse(data=course)


@course_router.put("/{id}")
@inject
async def update_course(
        id: int,
        course: CourseIn,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    course = await course_service.update_course(id, course)

    if not course:
        raise NotFoundException

    return UpdateResponse(data=course)


@course_router.delete("/{id}")
@inject
async def delete_course(
        id: int,
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    is_deleted = await course_service.delete_course(id)

    if not is_deleted:
        raise NotFoundException

    return DeleteResponse()


@course_router.post("/bulk")
@inject
async def create_courses(
        courses: List[CourseIn],
        course_service: CourseServiceContract = Depends(Provide[AdminContainer.course_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    await course_service.bulk_insert_courses(courses)

    return APIResponse()
