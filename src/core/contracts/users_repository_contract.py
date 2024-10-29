from abc import ABC, abstractmethod

from src.core.entities.user import User, UserBase


class UsersRepositoryContract(ABC):

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: UserBase) -> User:
        pass

    @abstractmethod
    async def create_new_user(
        self,
        username: str,
        full_name: str,
        email: str,
        password_hash: str,
    ) -> User:
        pass
