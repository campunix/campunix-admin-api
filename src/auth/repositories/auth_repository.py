from contextlib import AbstractContextManager
from typing import Callable
from src.auth.repositories.auth_repository_contract import AuthRepositoryContract
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.entities.auth.user import User, UserBase
from src.models.auth.user_models import UserOut


class AuthRepository(AuthRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_user_by_username(self, username: str) -> User:
        statement = select(User).where(User.username == username)
        result = await self.db_session.exec(statement)
        user = result.one_or_none()
        return user

    async def create_user(self, user: UserBase) -> User:
        new_user = User(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            password_hash=user.password_hash,
        )
        self.db_session.add(new_user)
        await self.db_session.commit()
        await self.db_session.refresh(new_user)
        return new_user
