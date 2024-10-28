from abc import ABC, abstractmethod
from typing import Any

from src.models.syllabus.syllabus_models import Course


class SyllabusRepositoryContract(ABC):

    @abstractmethod
    async def save(self, department_id: int, syllabus: dict[str, Any]):
        pass

    @abstractmethod
    async def get(self, course_code) -> Course:
        pass
