from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.user_organizations_repository_contract import UserOrganizationsRepositoryContract
from src.core.entities.user_organization import UserOrganization
from src.infrastructure.repositories.base_repository import BaseRepository


class UserOrganizationsRepository(BaseRepository[UserOrganization], UserOrganizationsRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, UserOrganization)