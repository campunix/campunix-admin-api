from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.features.auth.auth_container import AuthContainer
from src.models.user import Token, UserLogin, UserRegister
from src.features.auth.utils.oauth2_utils import oauth2_scheme

router = APIRouter()


@router.post("/token", response_model=Token, summary="Login to get access token")
@inject
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    token = await auth_service.authenticate_user(form_data.username, form_data.password)
    return token


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, summary="Register a new user"
)
@inject
async def register(
    register_data: UserRegister,
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    user = await auth_service.register_user(register_data)
    return user


@router.get("/me")
@inject
async def current_user(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    return await auth_service.get_current_user(token)


@router.get("/")
@inject
async def all_users(
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    return await auth_service.get_all_users()
