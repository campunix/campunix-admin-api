from abc import ABC, abstractmethod

class BookRepositoryContract(ABC):

    @abstractmethod
    def create_book(self, book):
        pass