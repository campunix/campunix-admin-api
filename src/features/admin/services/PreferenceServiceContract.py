from abc import abstractmethod, ABC
from typing import Optional, Dict, Any

from src.models.preference import PreferenceIn, PreferenceOut
from src.models.teacher import TeacherIn, TeacherOut


class PreferenceServiceContract(ABC):
    @abstractmethod
    async def create_preference(self, preference: PreferenceIn) -> Optional[PreferenceOut]:
        pass

    @abstractmethod
    async def get_preferences(self, page: int = 1, page_size: int = 10, paginate: bool = False)  -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_preference(self, id: int, preference: PreferenceIn) -> Optional[PreferenceOut]:
        pass

    @abstractmethod
    async def delete_preference(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_preference_by_id(self, id: int) -> Optional[PreferenceOut]:
        pass
