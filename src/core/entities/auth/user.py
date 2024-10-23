from datetime import datetime
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel
from src.core.entities.base_entity import BaseEntity


class UserBase(SQLModel):
    username: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False)
    full_name: str = Field(default=None, nullable=False)
    password_hash: str = Field(default=None, nullable=False)

class User(UserBase, table = True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now())
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), default=func.now(), onupdate=func.now()
        )
    )
