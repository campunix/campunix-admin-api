from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class StudentBase(SQLModel):
    user_id: int = Field(
        default=None,
        foreign_key="users.id",
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=True,
    )


class Student(BaseEntity, StudentBase, table=True):
    __tablename__ = "students"
