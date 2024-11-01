from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.organization_service_contract import OrganizationServiceContract
from src.models.organization import OrganizationIn

organization_router = APIRouter(prefix="/organizations")


@organization_router.post("")
@inject
async def create_organization(
        organization_in: OrganizationIn,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
):
    organization = await organization_service.create_organization(organization_in)
    return organization


@organization_router.get("")
@inject
async def get_all_organization(
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
):
    return await organization_service.get_organizations()


@organization_router.get("/{id}")
@inject
async def get_organization(
        id: int,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
):
    return await organization_service.get_organization_by_id(id)


@organization_router.put("/{id}")
@inject
async def update_organization(
        id: int,
        organization_in: OrganizationIn,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
):
    organization = await organization_service.update_organization(id, organization_in)
    return organization


@organization_router.delete("/{id}")
@inject
async def delete_organization(
        id: int,
        organization_service: OrganizationServiceContract = Depends(Provide[AdminContainer.organization_service]),
):
    organization = await organization_service.delete_organization(id)
    return organization
