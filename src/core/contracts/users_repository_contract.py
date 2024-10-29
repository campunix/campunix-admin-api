from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from src.core.entities.user import User, UserBase


class UsersRepositoryContract(ABC):

    @abstractmethod
    async def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_user_by_email_or_username(
        self, email_or_username: str
    ) -> Optional[User]:
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

    @abstractmethod
    async def get_all_users(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
    ) -> Dict[str, Any]:
        pass
