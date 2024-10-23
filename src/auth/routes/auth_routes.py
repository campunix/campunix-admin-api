from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, status
from src.auth.container.auth_container import AuthContainer
from src.auth.services.auth_service_contract import AuthServiceContract
from src.models.auth.user_models import Token, UserLogin, UserRegister

router = APIRouter()


@router.post("/login", response_model=Token, summary="Login to get access token")
@inject
async def login(
    login_data: UserLogin,
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    token = auth_service.authenticate_user(login_data.username, login_data.password)
    return token


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, summary="Register a new user"
)
@inject
async def register(
    register_data: UserRegister,
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    user = auth_service.register_user(register_data)
    return user
