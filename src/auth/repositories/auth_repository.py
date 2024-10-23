from contextlib import AbstractContextManager
from typing import Callable
from src.auth.repositories.auth_repository_contract import AuthRepositoryContract
from sqlalchemy.orm import Session

from src.core.entities.auth.user import User, UserBase
from src.models.auth.user_models import UserOut


class AuthRepository(AuthRepositoryContract):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    def get_user_by_username(self, username: str) -> UserOut:
        with self.session_factory() as session:
            user = session.query(User).filter(User.username == username).first()
            return self._user_entity_to_model(user)

    def create_user(self, user: UserBase) -> UserOut:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return self.get_user_by_username(user.username)

    def _user_entity_to_model(user: User) -> UserOut:
        return UserOut(
            id=user.id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
        )
