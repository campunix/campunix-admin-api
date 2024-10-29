from abc import ABC, abstractmethod
from typing import Any, Dict
from src.models.user_models import Token, UserOut, UserRegister


class AuthServiceContract(ABC):
    @abstractmethod
    def authenticate_user(self, username: str, password: str) -> Token:
        pass

    @abstractmethod
    async def register_user(self, userRegister: UserRegister) -> UserOut:
        pass

    @abstractmethod
    def get_current_user(self, token: str) -> UserOut:
        pass

    @abstractmethod
    def logout_user(self, token: str):
        pass

    @abstractmethod
    async def get_all_users(
        self, page: int = 1, page_size: int = 10, paginate: bool = False
    ) -> Dict[str, Any]:
        pass
