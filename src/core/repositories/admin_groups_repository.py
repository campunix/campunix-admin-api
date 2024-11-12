from src.core.contracts.admin_groups_repository_contract import AdminGroupsRepositoryContract
from src.core.entities.admin_group import AdminGroup
from src.infrastructure.repositories.base_repository import BaseRepository
from sqlmodel.ext.asyncio.session import AsyncSession

class AdminGroupsRepository(
    BaseRepository[AdminGroup], AdminGroupsRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, AdminGroup)