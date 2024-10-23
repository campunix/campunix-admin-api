from fastapi import APIRouter, Depends
from app.api.auth.services.auth_service import AuthService
from dependency_injector.wiring import inject, Provide
from app.api.auth.containers.auth_container import AuthContainer

auth_router = APIRouter()

@auth_router.post("/login")
@inject
async def login(username: str, password: str, service: AuthService = Depends(Provide[AuthContainer.auth_service])):
    return service.authenticate_user(username, password)