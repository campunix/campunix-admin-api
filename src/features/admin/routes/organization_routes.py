from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.authentication import UnauthenticatedUser

from src.core.entities.enums.user_role import UserRole
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.admin_service_contract import AdminServiceContract
from src.features.admin.services.organization_service_contract import OrganizationServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.organization import OrganizationIn
from src.models.response import APIResponse, CreateResponse, DeleteResponse, UpdateResponse
from src.models.user_organization import UserOrganizationIn
from src.utils.oauth2_utils import oauth2_scheme

organization_router = APIRouter(prefix="/organizations")


@organization_router.post("")
@inject
async def create_organization(
        organization_in: OrganizationIn,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
        admin_service: AdminServiceContract = Depends(Provide[AdminContainer.admin_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    organization = await organization_service.create_organization(organization_in)

    await admin_service.initiate_organization_for_current_user(token=token, organization_id=organization.id)

    return CreateResponse(data=organization)


@organization_router.get("")
@inject
async def get_all_organization(
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    organizations = await organization_service.get_organizations()
    return APIResponse(data=organizations)


@organization_router.get("/{id}")
@inject
async def get_organization(
        id: int,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    organization = await organization_service.get_organization_by_id(id)

    if not organization:
        raise NotFoundException

    return APIResponse(data=organization)


@organization_router.put("/{id}")
@inject
async def update_organization(
        id: int,
        organization_in: OrganizationIn,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    organization = await organization_service.update_organization(id, organization_in)

    if not organization:
        raise NotFoundException

    return UpdateResponse(data=organization)


@organization_router.delete("/{id}")
@inject
async def delete_organization(
        id: int,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    is_deleted = await organization_service.delete_organization(id)

    if not is_deleted:
        raise NotFoundException
    return DeleteResponse()


@organization_router.post("/{id}/link-user")
@inject
async def link_user(
        id: int,
        user_organization: UserOrganizationIn,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
        admin_service: AdminServiceContract = Depends(Provide[AdminContainer.admin_service]),
        token: str = Depends(oauth2_scheme),
        auth_service: AuthServiceContract = Depends(Provide[AdminContainer.auth_service]),
):
    user = await auth_service.get_current_user(token)

    if not user:
        raise UnauthenticatedUser

    organization = await organization_service.get_organization_by_id(id)

    if not organization:
        raise NotFoundException

    await admin_service.map_user_to_organization(
        organization_id=id,
        user_id=user_organization.user_id,
        role=UserRole.from_str(user_organization.role),
    )

    return APIResponse(message="User linked successfully")
