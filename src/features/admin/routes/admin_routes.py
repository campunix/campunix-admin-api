from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.admin_service_contract import AdminServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.utils.oauth2_utils import oauth2_scheme

admin_router = APIRouter(prefix="/admin")

@admin_router.get("")
@inject
async def check_admin(
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    return "admin routes"