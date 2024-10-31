from typing import List, Optional
from sqlmodel import SQLModel, Field

class Book(SQLModel):
    year: int
    title: str
    author: str
    publisher: str

class Module(SQLModel):
    module: str
    content: str

class Course(SQLModel):
    type: str
    books: List[Book]
    title: str
    credit: int
    modules: List[Module]
    outcomes: List[str]
    objectives: List[str]
    course_code: str
    prerequisite: str
    contact_hours: int

class Department(SQLModel):
    departmentID: int
    departmentCode: str
    departmentName: str

class SyllabusOut(SQLModel):
    courses: List[Course]
    semester: int
    department: Department
