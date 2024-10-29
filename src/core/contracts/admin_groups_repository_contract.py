from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from src.core.entities.admin_group import AdminGroup, AdminGroupBase


class AdminGroupsRepositoryContract(ABC):
    @abstractmethod
    async def createAdminGroup(self, admin_group: AdminGroupBase) -> AdminGroup:
        pass

    @abstractmethod
    async def get_admin_group_by_id(self, id: int) -> Optional[AdminGroup]:
        pass

    @abstractmethod
    async def get_all_admin_groups(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
        filters: Optional[List[Any]] = None, 
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_admin_group(self, id: id, admin_group: AdminGroupBase) -> AdminGroup:
        pass

    @abstractmethod
    async def delete_admin_group(self, id: id) -> bool:
        pass
