from abc import abstractmethod, ABC
from typing import Optional, Dict, Any

from src.models.preference import PreferenceIn, PreferenceOut


class PreferenceServiceContract(ABC):
    @abstractmethod
    async def create_preference(self, preference: PreferenceIn) -> Optional[PreferenceOut]:
        pass

    @abstractmethod
    async def get_preferences(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                              search_query: Optional[str] = None, ) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_preferences_by_teacher_id(self, teacher_id: int, page: int = 1, page_size: int = 10, paginate: bool = False,
                              search_query: Optional[str] = None, ) -> Dict[str, Any]:
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

    @abstractmethod
    async def get_days(self) -> Optional[Dict[str, Any]]:
        pass
