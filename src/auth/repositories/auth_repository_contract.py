from abc import ABC, abstractmethod

from src.core.entities.auth.user import User, UserBase

class AuthRepositoryContract(ABC):

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: UserBase) -> User:
        pass