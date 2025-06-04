from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.authentication import UnauthenticatedUser

from src.features.admin.admin_container import AdminContainer
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.features.auth.auth_container import AuthContainer
from src.models.response import APIResponse
from src.models.user import Token, UserLogin, UserRegister, ForgotPasswordRequest, ResetPasswordRequest, \
    ChangePasswordRequest
from src.features.auth.utils.auth_utils import oauth2_scheme

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
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    return user


@router.get("/users")
@inject
async def all_users(
        auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
        page: int = 1,
        page_size: int = 20,
        paginate: bool = True,
        query: str = "",
        token: str = Depends(oauth2_scheme)
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    users = await auth_service.get_all_users(page=page, page_size=page_size, paginate=paginate)
    return APIResponse(data=users)


@router.post("/forgot-password", summary="Request password reset")
@inject
async def forgot_password(
        request_data: ForgotPasswordRequest,
        auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    result = await auth_service.initiate_password_reset(request_data.email)
    return APIResponse(message="Password reset instructions sent.", status=result)


@router.post("/reset-password", summary="Reset password with token")
@inject
async def reset_password(
        request_data: ResetPasswordRequest,
        auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    result = await auth_service.reset_password(request_data.token, request_data)
    return APIResponse(message="Password has been reset successfully.", status=result)

@router.post("/change-password", summary="Change the password of the logged-in user")
@inject
async def change_password(
    request_data: ChangePasswordRequest,
    token: str = Depends(oauth2_scheme),
    auth_service: AuthServiceContract = Depends(Provide[AuthContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    result = await auth_service.change_password(user_id=user.id, data=request_data)
    return APIResponse(message="Password has been changed successfully.", status=result)