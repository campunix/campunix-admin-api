from typing import Any

from pydantic import validator, field_validator
from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.day import Day


class PreferenceBase(SQLModel):
    teacher_id: int = Field(
        default=None,
        foreign_key="teachers.user_id",
        nullable=False,
    )
    day: Day = Field(
        sa_column=Column(Enum(Day, name="day", create_type=False))
    )

    slot_no: int = Field(
        default=None,
        nullable=False
    )

    @field_validator("day", mode='before')
    def validate_day(cls, value: Any) -> Day:
        if isinstance(value, str):
            return Day.from_str(value)
        return value


class Preference(BaseEntity, PreferenceBase, table=True):
    __tablename__ = "preferences"
