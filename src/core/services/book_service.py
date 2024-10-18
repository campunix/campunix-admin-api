from src.core.contracts.book_repository_contract import BookRepositoryContract
from src.core.entities.book import Book
from src.models.request import BookInputModel

class BookService():
    def __init__(self, book_repository: BookRepositoryContract):
        self.book_repository = book_repository

    def get_books(self):
        book = Book()
        books = self.book_repository.read_by_options(book)
        return books.founds

    def create(self, input: BookInputModel):
        book = Book(
            id=input.id,
            title = input.title, 
            author = input.author)
        
        self.book_repository.create(book)