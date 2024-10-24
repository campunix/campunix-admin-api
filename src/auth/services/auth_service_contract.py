from abc import ABC, abstractmethod
from src.models.auth.user_models import Token, UserOut, UserRegister


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
