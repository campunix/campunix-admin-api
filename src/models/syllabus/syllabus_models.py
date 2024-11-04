from typing import List, Optional

from pydantic import BaseModel, Field


# Define Pydantic models
class Book(BaseModel):
    Title: Optional[str]
    Author: Optional[str]
    Publisher: Optional[str]
    Year: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class CourseDescription(BaseModel):
    Module: Optional[str]
    Content: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class Course(BaseModel):
    CourseCode: Optional[str]
    Title: Optional[str]
    Credit: Optional[float]
    Prerequisite: Optional[str]
    Type: Optional[str]
    ContactHours: Optional[int]
    Rationale: Optional[str]
    CourseObjectives: List[str] = []
    Outcomes: List[str] = []
    CourseDescription: List[CourseDescription] = []
    RecommendedBooks: List[Book] = []
    HardwareSoftwareRequirements: Optional[dict] = Field(default_factory=lambda: {"HW": None, "SW": None})

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class Semester(BaseModel):
    SemesterCode: int
    Courses: List[Course] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects


class SyllabusParsed(BaseModel):
    DepartmentID: int
    DepartmentCode: str
    DepartmentName: str
    Semesters: List[Semester] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True  # If you are using SQLAlchemy objects
