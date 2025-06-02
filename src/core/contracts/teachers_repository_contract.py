from abc import abstractmethod
from typing import Dict, Any

from src.core.contracts.base_repository_contract import BaseRepositoryContract


class TeachersRepositoryContract(BaseRepositoryContract):

    @abstractmethod
    async def get_teacher_designation(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_teacher_status(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def is_teacher(self, user_id: int) -> bool:
        pass
