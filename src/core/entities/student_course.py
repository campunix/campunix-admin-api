from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class StudentCourseBase(SQLModel):
    student_id: int = Field(
        default=None,
        foreign_key="students.id",
        nullable=False,
    )
    course_id: int = Field(
        default=None,
        foreign_key="courses.id",
        nullable=True,
    )


class StudentCourse(BaseEntity, StudentCourseBase, table=True):
    __tablename__ = "student_courses"
