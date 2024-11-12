from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.core.config import app_configs, settings
from src.features.admin.admin_container import AdminContainer
from src.features.admin.routes.admin_routes import admin_router
from src.features.admin.routes.course_routes import course_router
from src.features.admin.routes.department_routes import department_router
from src.features.admin.routes.organization_routes import organization_router
from src.features.admin.routes.room_routes import room_router
from src.features.admin.routes.teacher_course_routes import teacher_course_router
from src.features.admin.routes.teacher_routes import teacher_router
from src.features.auth.auth_container import AuthContainer
from src.features.auth.auth_routes import router as auth_router
from src.features.routine.routine_routes import router as routine_router
from src.models.response import APIResponse

app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=settings.CORS_ORIGINS,
    allow_origins=("*"),
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)


@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(APIResponse(status=False, code=exc.status_code, message=exc.detail))
    )


@app.get("/", include_in_schema=False)
async def index() -> dict[str, str]:
    return {"name": "Digital Library API"}


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

auth_container = AuthContainer()
admin_container = AdminContainer()

app.include_router(auth_router, tags=["auth"])
app.include_router(admin_router, tags=["admins"])
app.include_router(organization_router, tags=["organizations"])
app.include_router(department_router, tags=["departments"])
app.include_router(course_router, tags=["courses"])
app.include_router(room_router, tags=["rooms"])
app.include_router(teacher_router, tags=["teachers"])
app.include_router(teacher_course_router, tags=["teacherCourse"])
app.include_router(routine_router, tags=["routine"])