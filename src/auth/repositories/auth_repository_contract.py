from abc import ABC, abstractmethod

from src.core.entities.auth.user import UserBase
from src.models.auth.user_models import UserOut

class AuthRepositoryContract(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserOut:
        pass

    @abstractmethod
    def create_user(self, user: UserBase) -> UserOut:
        pass