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
def bearer_token():
    return (
        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NzkwMDc4MX0.qTDLLHKniVCfz-e847YYXsbmBRN50vbT_R37NmuLiz0"
    )


@pytest.fixture(scope="function")
async def authorized_client(bearer_token):
    async with AsyncClient(app=app, base_url="http://test") as client:
        client.headers.update({"Authorization": bearer_token})
        yield client
