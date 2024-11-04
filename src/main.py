from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import app_configs, settings
from src.features.admin.admin_container import AdminContainer
from src.features.admin.routes.admin_routes import admin_router
from src.features.admin.routes.course_routes import course_router
from src.features.admin.routes.department_routes import department_router
from src.features.admin.routes.organization_routes import organization_router
from src.features.auth.auth_container import AuthContainer
from src.features.auth.auth_routes import router as auth_router

app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)


@app.get("/", include_in_schema=False)
async def index() -> dict[str, str]:
    return {"name": "Digital Library API"}


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


auth_container = AuthContainer()
app.include_router(auth_router, tags=["auth"])

admin_container = AdminContainer()
app.include_router(admin_router, tags=["admins"])
app.include_router(organization_router, tags=["organizations"])
app.include_router(department_router, tags=["departments"])
app.include_router(course_router, tags=["courses"])