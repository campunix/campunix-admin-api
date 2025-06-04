import os
import smtplib
import uuid
from datetime import timedelta, datetime, timezone
from email.message import EmailMessage
from typing import Any, Dict
from fastapi import HTTPException, status
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.features.auth.utils.auth_utils import (
    create_access_token,
    get_password_hash,
    get_token_user,
    verify_password,
)
from src.core.contracts.users_repository_contract import UsersRepositoryContract
from src.core.entities.user import UserBase, user_entity_to_model
from src.models.user import Token, UserOut, UserRegister, ResetPasswordRequest, ChangePasswordRequest
from src.utils.oauth2_utils import ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context


class AuthService(AuthServiceContract):
    def __init__(self, users_repository: UsersRepositoryContract):
        self.repository = users_repository

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
        return user_entity_to_model(
            await self.repository.get_user_by_username(await get_token_user(token))
        )

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

        new_user = await self.repository.create_new_user(
            username=username,
            full_name=full_name,
            email=email,
            password_hash=hashed_password,
        )

        return user_entity_to_model(new_user)

    async def get_all_users(
            self, page: int = 1, page_size: int = 10, paginate: bool = False
    ) -> Dict[str, Any]:
        return await self.repository.get_all_users(
            page=page,
            page_size=page_size,
            paginate=paginate,
        )

    def logout_user(self, token: str):
        raise NotImplementedError("Logout functionality is not implemented.")

    async def initiate_password_reset(self, email: str) -> bool:
        user = await self.repository.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        reset_token = str(uuid.uuid4())
        token_expiry = datetime.now(timezone.utc) + timedelta(hours=1)

        await self.repository.save_reset_token(user.id, reset_token, token_expiry)

        reset_link = f"http://localhost:4200/reset-password?token={reset_token}"

        # Compose email
        message = EmailMessage()
        message["Subject"] = "Password Reset Request"
        message["From"] = os.getenv("GMAIL_USERNAME")
        message["To"] = email
        message.set_content(
            f"Hi {user.full_name},\n\n"
            f"Click the link below to reset your password:\n\n{reset_link}\n\n"
            f"This link will expire in 1 hour.\n\n"
            f"If you didn't request this, you can ignore this email."
        )

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.getenv("GMAIL_USERNAME"), os.getenv("GMAIL_APP_PASSWORD"))
                server.send_message(message)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to send reset email: {str(e)}"
            )

        return True

    async def reset_password(self, token: str, request_data: ResetPasswordRequest) -> bool:
        if request_data.new_password != request_data.confirm_password:
            raise HTTPException(
                status_code=400,
                detail="New password and confirm password do not match"
            )

        user = await self.repository.get_by_reset_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if user.reset_token_expiry < datetime.now(timezone.utc):
            raise HTTPException(
                status_code=400,
                detail="Invalid or expired token"
            )

        password_hash = pwd_context.hash(request_data.new_password)
        await self.repository.update_password(user.id, password_hash)
        await self.repository.clear_reset_token(user.id)

        return True

    async def change_password(self, user_id: int, data: ChangePasswordRequest) -> bool:
        if data.new_password != data.confirm_password:
            raise HTTPException(
                status_code=400,
                detail="New password and confirm password do not match"
            )

        user = await self.repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if not verify_password(data.current_password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is incorrect"
            )

        new_password_hash = get_password_hash(data.new_password)
        await self.repository.update_password(user_id, new_password_hash)

        return True


