from src.core.contracts.organizations_repository_contract import (
    OrganizationsRepositoryContract,
)
from src.core.entities.organization import Organization
from src.infrastructure.repositories.base_repository import BaseRepository
from sqlmodel.ext.asyncio.session import AsyncSession


class OrganizationsRepository(
    BaseRepository[Organization], OrganizationsRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Organization)
