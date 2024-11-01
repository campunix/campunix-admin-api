from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.department_service_contract import DepartmentServiceContract
from src.models.department import DepartmentIn

department_router = APIRouter(prefix="/departments")

@department_router.post("")
@inject
async def create_department(
        department: DepartmentIn,
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):
    return await department_service.create_department(department)


@department_router.get("")
@inject
async def get_all_departments(
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):
    return await department_service.get_departments()


@department_router.get("/{id}")
@inject
async def get_organization(
        id: int,
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):
    return await department_service.get_department_by_id(id)


@department_router.put("/{id}")
@inject
async def update_organization(
        id: int,
        department: DepartmentIn,
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):

    return await department_service.update_department(id, department)


@department_router.delete("/{id}")
@inject
async def delete_organization(
        id: int,
        department_service: DepartmentServiceContract = Depends(Provide[AdminContainer.department_service]),
):
    return await department_service.delete_department(id)
