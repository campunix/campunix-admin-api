from enum import Enum


class CourseType(str, Enum):
    THEORY = "THEORY"
    LAB = "LAB"
    RESEARCH = "RESEARCH"
    VIVA = "VIVA"

    @classmethod
    def from_str(cls, type_str: str):
        try:
            return cls[type_str]
        except KeyError:
            raise ValueError(f"Invalid type: {type_str}")