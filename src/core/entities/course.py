from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.course_type import CourseType


class CourseBase(SQLModel):
    title: str = Field(
        default=None,
        nullable=False,
    )
    code: str = Field(
        default=None,
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=False,
    )
    course_type: CourseType = Field(
        sa_column=Column(Enum(CourseType, name="course_type", create_type=False))
    )


class Course(BaseEntity, CourseBase, table=True):
    __tablename__ = "courses"