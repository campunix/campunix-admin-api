from sqlalchemy import Column, JSON
from sqlmodel import SQLModel, Field

from src.core.entities.base_entity import BaseEntity


class RoutineBase(SQLModel):
    syllabus_id: int = Field(
        default=None,
        foreign_key="syllabuses.id",
        nullable=False
    )

    title: str = Field(
        default=None,
        nullable=True,
    )

    description: str = Field(
        default=None,
        nullable=True,
    )

    calendar_year: str = Field(
        default=None,
        nullable=True,
    )

    is_active: bool = Field(
        default=False,
        nullable=False,
    )

    routine: dict = Field(default=None, sa_column=Column(JSON))

class Routine(BaseEntity, RoutineBase, table=True):
    __tablename__ = "routines"