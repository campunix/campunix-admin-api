import os
import sys
from unittest.mock import AsyncMock
from unittest.mock import patch

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.features.admin.admin_container import AdminContainer
from src.main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


@pytest.fixture(scope="session")
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_session():
    engine = create_async_engine("postgresql+asyncpg://postgres:1qazZAQ!@localhost/campunix_admin", echo=True)
    async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session_maker() as session:
        yield session
    await engine.dispose()


@pytest.fixture
def organization_service_mock():
    with patch.object(AdminContainer, "organization_service") as mock:
        mock.return_value = AsyncMock()
        yield mock.return_value


@pytest.fixture
def admin_service_mock():
    with patch.object(AdminContainer, "admin_service") as mock:
        mock.return_value = AsyncMock()
        yield mock.return_value


@pytest.fixture
def preference_service_mock():
    with patch.object(AdminContainer, "preference_service") as mock:
        mock.return_value = AsyncMock()
        yield mock.return_value


@pytest.fixture
def room_service_mock():
    with patch.object(AdminContainer, "room_service") as mock:
        mock.return_value = AsyncMock()
        yield mock.return_value

@pytest.fixture
def department_service_mock():
    with patch.object(AdminContainer, "department_service") as mock:
        mock.return_value = AsyncMock()
        yield mock.return_value


@pytest.fixture
def bearer_token():
    return (
        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NzkwMDc4MX0.qTDLLHKniVCfz-e847YYXsbmBRN50vbT_R37NmuLiz0"
    )


@pytest.fixture(scope="function")
async def authorized_client(bearer_token):
    async with AsyncClient(app=app, base_url="http://test") as client:
        client.headers.update({"Authorization": bearer_token})
        yield client
