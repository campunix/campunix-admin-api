from typing import List, Optional

from pydantic import BaseModel, Field


# Define Pydantic models
class Book(BaseModel):
    title: Optional[str]
    author: Optional[str]
    publisher: Optional[str]
    year: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class CourseDescription(BaseModel):
    module: Optional[str]
    content: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class Course(BaseModel):
    course_code: Optional[str]
    title: Optional[str]
    credit: Optional[float]
    prerequisite: Optional[str]
    type: Optional[str]
    contact_hours: Optional[int]
    rationale: Optional[str]
    course_objectives: List[str] = []
    outcomes: List[str] = []
    course_description: List[CourseDescription] = []
    recommended_books: List[Book] = []
    hardware_software_requirements: Optional[dict] = Field(default_factory=lambda: {"HW": None, "SW": None})

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class Semester(BaseModel):
    year: int
    number: int
    courses: List[Course] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class SyllabusParsed(BaseModel):
    department_code: str
    department_name: str
    semesters: List[Semester] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects
