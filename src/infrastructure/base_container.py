from dependency_injector import containers, providers

from src.core.repositories.admin_groups_repository import AdminGroupsRepository
from src.core.repositories.departments_repository import DepartmentsRepository
from src.core.repositories.organizations_repository import OrganizationsRepository
from src.core.repositories.user_organizations_repository import UserOrganizationsRepository
from src.core.repositories.users_repository import UsersRepository
from src.infrastructure.database2 import Database2


class BaseContainer(containers.DeclarativeContainer):
    db = providers.Singleton(Database2)
    db_session = providers.Resource(db.provided.get_session())

    organizations_repository = providers.Factory(
        OrganizationsRepository, db_session=db_session
    )

    admin_groups_repository = providers.Factory(
        AdminGroupsRepository, db_session=db_session
    )

    departments_repository = providers.Factory(
        DepartmentsRepository, db_session=db_session
    )

    user_organizations_repository = providers.Factory(
        UserOrganizationsRepository, db_session=db_session
    )

    users_repository = providers.Factory(UsersRepository, db_session=db_session)
