from src.core.contracts.users_repository_contract import UsersRepositoryContract
from src.core.entities.user import User, UserBase
from sqlmodel.ext.asyncio.session import AsyncSession


class FakeUsersRepository(UsersRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        pass

    async def get_user_by_username(self, username: str) -> User:
        if username == "fake":
            return User(
                username="fake",
                email="fake@email.com",
                full_name="totally fake",
                password_hash="password_hash",
            )

        return None

    async def create_user(self, user: UserBase) -> User:
        return user

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
