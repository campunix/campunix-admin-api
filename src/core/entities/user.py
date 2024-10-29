from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.models.user_models import UserOut


class UserBase(SQLModel):
    username: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False)
    full_name: str = Field(default=None, nullable=False)
    password_hash: str = Field(default=None, nullable=False)


class User(BaseEntity, UserBase, table=True):
    __tablename__ = "users"


def user_entity_to_model(user: User) -> UserOut:
    if user:
        return UserOut(
            id=user.id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
        )
    return None
