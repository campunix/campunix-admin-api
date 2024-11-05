from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import app_configs, settings
from src.features.auth.auth_container import AuthContainer
from src.features.auth.auth_routes import router as auth_router
from src.features.routine.routine_routes import router as routine_router

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

@app.get("/", include_in_schema=False)
async def index() -> dict[str, str]:
    return {"name": "Digital Library API"}

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

auth_container = AuthContainer()
app.include_router(auth_router, tags=["auth"])
app.include_router(routine_router, tags=["routine"])