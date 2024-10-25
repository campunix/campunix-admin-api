from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.contracts.users_repository_contract import UsersRepositoryContract
from src.core.entities.auth.user import User, UserBase


class UsersRepository(UsersRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_user_by_username(self, username: str) -> User:
        statement = select(User).where(User.username == username)
        result = await self.db_session.exec(statement)
        user = result.one_or_none()
        return user

    async def get_user_by_email(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        result = await self.db_session.exec(statement)
        user = result.one_or_none()
        return user

    async def get_user_by_email_or_username(self, email_or_username: str) -> User:
        statement = select(User).where(
            User.email == email_or_username or User.username == email_or_username
        )
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
