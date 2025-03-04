from datetime import datetime

from sqlalchemy import Column, DateTime, func, JSON
from sqlmodel import Field, SQLModel


class SyllabusBase(SQLModel):
    department_id: int = Field(default=None, nullable=False)
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
    syllabus: dict = Field(default=None, sa_column=Column(JSON))


class Syllabus(SyllabusBase, table=True):
    __tablename__ = "syllabuses"

    id: int = Field(default=None, nullable=False, primary_key=True)

    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now())
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), default=func.now(), onupdate=func.now()
        )
    )
