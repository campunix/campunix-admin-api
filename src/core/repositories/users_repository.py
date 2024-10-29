from typing import Any, Dict, Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.contracts.users_repository_contract import UsersRepositoryContract
from src.core.entities.user import User, UserBase
from src.infrastructure.repositories.base_repository import BaseRepository


class UsersRepository(BaseRepository[User], UsersRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, User)

    async def get_user_by_username(self, username: str) -> Optional[User]:
        statement = select(User).where(User.username == username)
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_user_by_email(self, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_user_by_email_or_username(
        self, email_or_username: str
    ) -> Optional[User]:
        statement = select(User).where(
            (User.email == email_or_username) | (User.username == email_or_username)
        )
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def create_user(self, user: UserBase) -> User:
        new_user = User(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            password_hash=user.password_hash,
        )
        return await self.create(new_user)

    async def create_new_user(
        self,
        username: str,
        full_name: str,
        email: str,
        password_hash: str,
    ) -> User:
        new_user = User(
            username=username,
            full_name=full_name,
            email=email,
            password_hash=password_hash,
        )

        return await self.create_user(new_user)

    async def get_all_users(
        self, page: int = 1, page_size: int = 10, paginate: bool = False
    ) -> Dict[str, Any]:
        return await self.get_all(page=page, page_size=page_size, paginate=paginate)
