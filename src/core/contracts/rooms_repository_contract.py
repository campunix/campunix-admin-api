from typing import Dict, Any

from src.core.contracts.base_repository_contract import BaseRepositoryContract


class RoomsRepositoryContract(BaseRepositoryContract):

    async def get_room_types(self) -> Dict[str, Any]:
        pass
