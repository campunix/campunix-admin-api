from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from src.core.contracts.book_repository_contract import BookRepositoryContract
from src.core.entities.book import Book
from src.infrastructure.repositories.base_repository import BaseRepository

class BookRepository(BookRepositoryContract, BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Book)

    def create_book(self, book):
        self.create(book)