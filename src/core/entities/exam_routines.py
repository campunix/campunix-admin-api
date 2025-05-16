from typing import List
from sqlalchemy import Column, JSON
from src.core.entities.base_entity import BaseEntity
from sqlmodel import SQLModel, Field, Relationship


class ExamRoutineBase(SQLModel):
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

    exam_routine: dict = Field(default=None, sa_column=Column(JSON))


class ExamRoutine(BaseEntity, ExamRoutineBase, table=True):
    __tablename__ = "exam_routines"
