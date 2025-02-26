from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.department_service_contract import DepartmentServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.department import DepartmentIn, DepartmentCreate
from src.models.response import CreateResponse, APIResponse, DeleteResponse, ErrorResponse, UpdateResponse
from src.utils.oauth2_utils import oauth2_scheme

department_router = APIRouter(prefix="/departments")


@department_router.post("")
@inject
async def create_department(
        department: DepartmentCreate,
        token: str = Depends(oauth2_scheme),
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    department = await department_service.create_department(
        department=DepartmentIn(
            name=department.name,
            code=department.code,
            organization_id=department.organization_id,
            created_by=user.id
        ),
    )

    return CreateResponse(data=department)


@department_router.get("")
@inject
async def get_all_departments(
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None
):
    departments = await department_service.get_departments(page=page, page_size=page_size, paginate=True, search_query=search_query)
    return APIResponse(data=departments)


@department_router.get("/{id}")
@inject
async def get_department(
        id: int,
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):
    department = await department_service.get_department_by_id(id)
    return APIResponse(data=department)


@department_router.put("/{id}")
@inject
async def update_department(
        id: int,
        department: DepartmentCreate,
        token: str = Depends(oauth2_scheme),
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    department = await department_service.update_department(
        id=id,
        department=DepartmentIn(
            name=department.name,
            code=department.code,
            organization_id=department.organization_id,
            created_by=user.id
        ),
    )

    if not department:
        raise NotFoundException

    return UpdateResponse(data=department)


@department_router.delete("/{id}")
@inject
async def delete_department(
        id: int,
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):
    is_deleted = await department_service.delete_department(id)
    if not is_deleted:
        raise NotFoundException

    return DeleteResponse()
