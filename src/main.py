from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.infrastructure.container import Container
from src.routers.books import router as book_router
from src.core.config import app_configs, settings

app = FastAPI(**app_configs)

container = Container()

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

app.include_router(book_router, tags=["Book"])