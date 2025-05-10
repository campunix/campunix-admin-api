from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from src.models.exam_routine import ExamRoutineOut, ExamRoutineIn


class ExamRoutineServiceContract(ABC):
    @abstractmethod
    async def save_exam_routine(self, exam_routine_in: ExamRoutineIn) -> Optional[ExamRoutineOut]:
        pass

    @abstractmethod
    async def get_exam_routines(
            self,
            page: int = 1,
            page_size: int = 10,
            paginate: bool = False,
            search_query: Optional[str] = None
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_exam_routine_by_id(self, id: int) -> Optional[ExamRoutineOut]:
        pass

    @abstractmethod
    async def update_exam_routine(self, id: int, exam_routine_in: ExamRoutineIn) -> Optional[ExamRoutineOut]:
        pass

    @abstractmethod
    async def delete_exam_routine(self, id: int) -> bool:
        pass
