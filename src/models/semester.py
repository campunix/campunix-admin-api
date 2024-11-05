from pydantic import BaseModel


class SemesterOut(BaseModel):
    id: int
    year: int
    number: int
    disabled: bool


class SemesterIn(BaseModel):
    year: int
    number: int
    disabled: bool
    department_id: int


class SemesterCreate(BaseModel):
    year: int
    number: int
