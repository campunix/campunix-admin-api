from dependency_injector import containers, providers

from src.infrastructure.database2 import Database2


class BaseContainer(containers.DeclarativeContainer):
    pass