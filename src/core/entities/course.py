from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.course_type import CourseType


class CourseBase(SQLModel):
    name: str = Field(
        default=None,
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=False,
    )
    course_type: CourseType = Field(
        default=None,
        sa_column=Column(Enum(CourseType)),
        nullable=False,
    )


class Course(BaseEntity, CourseBase, table=True):
    __tablename__ = "courses"