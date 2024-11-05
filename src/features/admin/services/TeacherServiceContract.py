from abc import abstractmethod, ABC
from typing import Optional

from src.models.teacher import TeacherIn, TeacherOut


class TeacherServiceContract(ABC):
    @abstractmethod
    async def create_teacher(self, teacher: TeacherIn) -> Optional[TeacherOut]:
        pass

    @abstractmethod
    async def get_teachers(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        pass

    @abstractmethod
    async def update_teacher(self, id: int, teacher: TeacherIn) -> Optional[TeacherOut]:
        pass

    @abstractmethod
    async def delete_teacher(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_teacher_by_id(self, id: int) -> Optional[TeacherOut]:
        pass
