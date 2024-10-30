from dependency_injector import containers, providers

from src.infrastructure.database2 import Database2

class BaseContainer(containers.DeclarativeContainer):
    db = providers.Singleton(Database2)
    db_session = providers.Resource(db.provided.get_session())