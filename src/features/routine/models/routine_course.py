from pydantic import BaseModel


class RoutineCourse:
    id: int
    title: str
    code: str
    course_type: str
    is_lab: bool

    def __init__(self, id: int, title: str, code: str, course_type: str):
        self.id = id
        self.title = title
        self.code = code
        self.course_type = course_type
        self.is_lab = course_type is 'LAB'