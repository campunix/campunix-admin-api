from dependency_injector import containers, providers

from src.core.services.book_service import BookService
from src.infrastructure.database import Database
from src.infrastructure.repositories.book_repository import BookRepository
from src.core.config import settings

# Import your services and repositories
class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "__main__",
        "src.routers.books"])

    db = providers.Singleton(Database, db_url=str(settings.DATABASE_URL))

    # Define a provider for the BookRepository
    book_repository = providers.Factory(
        BookRepository,
        session_factory=db.provided.session
    )

    # Define a provider for the BookService
    book_service = providers.Factory(
        BookService,
        book_repository = book_repository
    )