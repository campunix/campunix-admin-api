from abc import ABC, abstractmethod

from fastapi import File

from src.core.entities.syllabus.syllabus import Syllabus
from src.models.syllabus.syllabus_models import Course


class SyllabusServiceContract(ABC):

    @abstractmethod
    async def save(self, file: File(...)) -> Syllabus:
        pass

    @abstractmethod
    def get(self, course_code: str) -> Course:
        pass
