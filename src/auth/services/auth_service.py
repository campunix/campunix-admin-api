from datetime import timedelta
from fastapi import HTTPException, status
from src.auth.repositories.auth_repository_contract import AuthRepositoryContract
from src.auth.services.auth_service_contract import AuthServiceContract
from src.auth.services.auth_service_core import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_password_hash,
    get_token_user,
    verify_password,
)
from src.core.entities.auth.user import UserBase, user_entity_to_model
from src.models.auth.user_models import Token, UserOut, UserRegister


class AuthService(AuthServiceContract):
    def __init__(self, repository: AuthRepositoryContract):
        self.repository = repository

    async def authenticate_user(self, username: str, password: str) -> Token:
        user = await self.repository.get_user_by_username(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username},
            expires_delta=access_token_expires,
        )

        return Token(access_token=access_token, token_type="Bearer")

    async def get_current_user(self, token: str) -> UserOut:
        return user_entity_to_model(await self.repository.get_user_by_username(await get_token_user(token)))

    async def register_user(self, userRegister: UserRegister) -> UserOut:
        email = userRegister.email
        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email is empty!",
            )

        username = userRegister.username
        if not username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username is empty!",
            )

        full_name = userRegister.full_name
        if not full_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Full name is empty!",
            )

        password = userRegister.password
        if not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password is empty!",
            )

        confirm_password = userRegister.confirm_password
        if not confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Confirm password is empty!",
            )

        if password != confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password did not matched!",
            )

        user = await self.repository.get_user_by_username(username)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )

        hashed_password = get_password_hash(password)

        new_user = await self.repository.create_user(
            UserBase(
                username=username,
                full_name=full_name,
                email=email,
                password_hash=hashed_password,
            )
        )

        return user_entity_to_model(new_user)

    def logout_user(self, token: str):
        raise NotImplementedError("Logout functionality is not implemented.")