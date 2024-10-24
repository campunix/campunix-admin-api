from datetime import datetime
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel

from src.models.auth.user_models import UserOut

class UserBase(SQLModel):
    username: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False)
    full_name: str = Field(default=None, nullable=False)
    password_hash: str = Field(default=None, nullable=False)


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now())
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), default=func.now(), onupdate=func.now()
        )
    )


def user_entity_to_model(user: User) -> UserOut:
    if user:
        return UserOut(
            id=user.id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
        )
    return None
