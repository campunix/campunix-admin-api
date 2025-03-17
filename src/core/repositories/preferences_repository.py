from typing import Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.preferences_repository_contract import PreferencesRepositoryContract
from src.core.entities.preference import Preference
from src.infrastructure.repositories.base_repository import BaseRepository
from src.core.entities.enums.day import Day


class PreferencesRepository(
    BaseRepository[Preference], PreferencesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Preference)

    async def get_days(self) -> Dict[str, Any]:
        return {"items": [room.name for room in Day]}
