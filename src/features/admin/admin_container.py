from dependency_injector import containers, providers

from src.features.admin.services.admin_service import AdminService
from src.features.admin.services.course_service import CourseService
from src.features.admin.services.department_service import DepartmentService
from src.features.admin.services.organization_service import OrganizationService
from src.features.admin.services.semester_service import SemesterService
from src.features.auth.services.auth_service import AuthService
from src.infrastructure.base_container import BaseContainer


class AdminContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(packages=["."])

    auth_service = providers.Factory(
        AuthService,
        users_repository=BaseContainer.users_repository,
    )

    admin_service = providers.Factory(
        AdminService,
        user_organizations_repository=BaseContainer.user_organizations_repository,
        admin_groups_repository=BaseContainer.admin_groups_repository,
        auth_service=auth_service,
    )

    organization_service = providers.Factory(
        OrganizationService,
        organizations_repository=BaseContainer.organizations_repository,
    )

    department_service = providers.Factory(
        DepartmentService,
        departments_repository=BaseContainer.departments_repository,
    )

    semester_service = providers.Factory(
        SemesterService,
        semester_repository=BaseContainer.semesters_repository
    )

    course_service = providers.Factory(
        CourseService,
        course_repository=BaseContainer.courses_repository
    )
