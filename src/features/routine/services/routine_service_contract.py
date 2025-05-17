from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from src.features.routine.models.routine_in import SavedRoutineIn
from src.features.routine.models.routine_out import SavedRoutineOut


class RoutineServiceContract(ABC):
    @abstractmethod
    async def generate_routine_async(self, syllabus_id: int, total_slots: int):
        pass

    @abstractmethod
    async def save_routine(self, routine_save_in: SavedRoutineIn) -> Optional[SavedRoutineOut]:
        pass

    @abstractmethod
    async def delete_routine(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_routine_by_id(self, id: int) -> Optional[SavedRoutineOut]:
        pass

    @abstractmethod
    async def get_saved_routines(
        self,
        page: int = 1, 
        page_size: int = 10, 
        paginate: bool = False,
        search_query: Optional[str] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_saved_routine(self, id: int, routine_save_in: SavedRoutineIn) -> Optional[SavedRoutineOut]:
        pass
