from pydantic import BaseModel


class SemesterOut(BaseModel):
    id: int
    year: int
    number: int


class SemesterIn(BaseModel):
    year: int
    number: int
    department_id: int

class SemesterCreate(BaseModel):
    year: int
    number: int