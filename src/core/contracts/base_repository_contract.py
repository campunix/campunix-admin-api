from abc import ABC
from typing import Any, Dict, List, Optional, TypeVar

from sqlmodel import SQLModel

T = TypeVar("T", bound=SQLModel)


class BaseRepositoryContract(ABC):
    async def get_by_id(self, id: int) -> Optional[T]:
        pass

    async def get_all(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
        filters: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        pass

    async def create(self, obj: T) -> T:
        pass

    async def update(self, id: int, obj_data: T) -> Optional[T]:
        pass

    async def delete(self, id: int) -> bool:
        pass
