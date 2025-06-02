from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class TeacherCourseBase(SQLModel):
    teacher_id: int = Field(
        default=None,
        foreign_key="teachers.id",
        nullable=False,
    )
    course_id: int = Field(
        default=None,
        foreign_key="courses.id",
        nullable=False,
    )


class TeacherCourse(BaseEntity, TeacherCourseBase, table=True):
    __tablename__ = "teacher_courses"
