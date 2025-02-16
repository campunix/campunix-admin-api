from typing import List

from sqlmodel import Field, SQLModel, Relationship

from src.core.entities.base_entity import BaseEntity
from src.core.entities.course import Course
from src.core.entities.exam_routine.exam_routine_course_teachers import ExamRoutineCourseTeacher
from src.core.entities.exam_routine.exam_routines import ExamRoutine


class ExamRoutineCourseBase(SQLModel):
    exam_routine_id: int = Field(
        default=None, foreign_key="exam_routines.id", nullable=False
    )
    course_id: int = Field(
        default=None, foreign_key="courses.id", nullable=False
    )


class ExamRoutineCourse(BaseEntity, ExamRoutineCourseBase, table=True):
    __tablename__ = "exam_routine_courses"

    exam_routine: ExamRoutine = Relationship(back_populates="exam_routine_courses")
    exam_course: Course = Relationship(back_populates="exam_routine_courses")
    exam_routine_course_teachers: List["ExamRoutineCourseTeacher"] = Relationship(
        back_populates="exam_routine_courses"
    )
