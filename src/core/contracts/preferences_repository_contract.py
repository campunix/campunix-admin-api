from typing import Dict, Any

from src.core.contracts.base_repository_contract import BaseRepositoryContract


class PreferencesRepositoryContract(BaseRepositoryContract):

    async def get_days(self) -> Dict[str, Any]:
        pass
