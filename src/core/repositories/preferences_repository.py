from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.preferences_repository_contract import PreferencesRepositoryContract
from src.core.entities.preference import Preference
from src.infrastructure.repositories.base_repository import BaseRepository


class PreferencesRepository(
    BaseRepository[Preference], PreferencesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Preference)
