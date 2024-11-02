from enum import Enum


class CourseType(str, Enum):
    THEORY = "THEORY"
    LAB = "LAB"
    RESEARCH = "RESEARCH"
    VIVA = "VIVA"