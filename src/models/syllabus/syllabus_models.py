from typing import List, Optional, Any
from pydantic import BaseModel


class Book(BaseModel):
    Title: str
    Author: str
    Publisher: str
    Year: int


class RecommendedBooks(BaseModel):
    Books: List[Book]


class Module(BaseModel):
    Module: str
    Content: str


class CourseDescription(BaseModel):
    Modules: List[Module]


class HardwareSoftwareRequirements(BaseModel):
    HW: str
    SW: str


class CourseObjectives(BaseModel):
    Objectives: List[str]


class LearningOutcomes(BaseModel):
    Outcomes: List[str]


class Course(BaseModel):
    CourseCode: str
    Title: str
    Credit: float
    Prerequisite: Optional[str] = None
    Type: str
    ContactHours: int
    Rationale: str
    CourseObjectives: CourseObjectives
    StudentLearningOutcomes: Optional[LearningOutcomes] = None
    LabOutcomes: Optional[LearningOutcomes] = None
    CourseDescription: Optional[CourseDescription] = None
    RecommendedBooks: Optional[RecommendedBooks] = None
    HardwareSoftwareRequirements: Optional[HardwareSoftwareRequirements] = None


class SyllabusOut(BaseModel):
    Department: str
    Semester: str
    Courses: dict[str, Any]
