from typing import List

from src.core.entities.base_entity import BaseEntity
from sqlmodel import SQLModel, Field, Relationship

from src.core.entities.exam_routine.exam_routine_courses import ExamRoutineCourse


class ExamRoutineBase(SQLModel):
    title: str = Field(default=None)
    description: str = Field(default=None)


class ExamRoutine(BaseEntity, ExamRoutineBase, table=True):
    __tablename__ = "exam_routines"

    exam_routine_courses: List["ExamRoutineCourse"] = Relationship(
        back_populates="exam_routines"
    )
