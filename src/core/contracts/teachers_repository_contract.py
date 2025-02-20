from typing import Dict, Any

from src.core.contracts.base_repository_contract import BaseRepositoryContract


class TeachersRepositoryContract(BaseRepositoryContract):

    async def get_teacher_designation(self) -> Dict[str, Any]:
        pass

    async def get_teacher_status(self) -> Dict[str, Any]:
        pass
