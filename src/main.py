from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import app_configs, settings
from src.features.auth.auth_container import AuthContainer
from src.features.auth.auth_routes import router as auth_router
from src.features.syllabus.syllabus_container import SyllabusContainer
from src.features.syllabus.syllabus_routes import router as syllabus_router

app = FastAPI(**app_configs)

# container = Container()

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
syllabus_container = SyllabusContainer()

app.include_router(auth_router, tags=["auth"])
app.include_router(syllabus_router, tags=["syllabus"])