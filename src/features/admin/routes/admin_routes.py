from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.admin_service_contract import AdminServiceContract

admin_router = APIRouter(prefix="/admin")

@admin_router.get("")
@inject
async def check_admin(
        admin_service: AdminServiceContract = Depends(Provide[AdminContainer.admin_service]),
):
    return "admin routes"