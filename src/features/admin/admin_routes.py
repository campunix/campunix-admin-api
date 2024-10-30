from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.admin_service_contract import AdminServiceContract


router = APIRouter(prefix="/admin")
