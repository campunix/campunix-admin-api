from pydantic import BaseModel

from src.features.routine.models.chromosome import Chromosome
from src.features.routine.models.routine_course import RoutineCourse
from src.features.routine.models.routine_semester import RoutineSemester

class RoutineOut:
    courses: list[RoutineCourse]
    semesters: list[RoutineSemester]
    routine: Chromosome

    def __init__(self, courses, semesters, routine):
        self.courses = courses
        self.semesters = semesters
        self.routine = routine
