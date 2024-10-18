from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, status, Path

from src.core.services.book_service import BookService
from src.infrastructure.container import Container
from src.models.request import BookInputModel
from src.models.response import CommandResponse

from src.models.query import QueryResponse

router = APIRouter()

@router.get("/books")
@inject
def get_books(sk: str = None, page: int = 1, book_service: BookService = Depends(Provide[Container.book_service])) -> QueryResponse:
    limit = 10
    skip = (page - 1) * limit
    return book_service.get_books()

@router.post("/books", status_code=status.HTTP_201_CREATED)
@inject
def create_book(book: BookInputModel, book_service: BookService = Depends(Provide[Container.book_service])):

    book_service.create(book)

    return CommandResponse(success=True, message="Book created successfully!")
