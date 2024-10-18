import pytest
from async_asgi_testclient import TestClient
from fastapi import status

@pytest.mark.asyncio
async def test_book_creation(client: TestClient) -> None:
    resp = await client.post(
        "/books",
        json={
            "title": "The Kite Runner",
            "author": "Test Author",
            "publication_year": 2000,
            "summary": "Test summary"
        }
    )

    assert resp.status_code == status.HTTP_201_CREATED

# More unit test will be added here.