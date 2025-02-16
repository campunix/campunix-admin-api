from email.policy import default

from sqlmodel import SQLModel, Field, Relationship

from src.core.entities.base_entity import BaseEntity
from src.core.entities.exam_routine.exam_routine_courses import ExamRoutineCourse
from src.core.entities.teacher import Teacher


class ExamRoutineCourseTeacherBase(SQLModel):
    exam_routine_course_id: int = Field(
        default=None, foreign_key="exam_routine_courses.id", nullable=False
    )
    teacher_id: int = Field(
        default=None, foreign_key="teachers.id", nullable=False
    )
    is_chief: bool = Field(default=False)


class ExamRoutineCourseTeacher(BaseEntity, ExamRoutineCourseTeacherBase, table=True):
    __tablename__ = "exam_routine_course_teachers"

    exam_routine_course: ExamRoutineCourse = Relationship(back_populates="exam_routine_course_teachers")
    teacher: Teacher = Relationship(back_populates="exam_routine_courses")
