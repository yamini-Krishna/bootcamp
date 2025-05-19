from abc import ABC, abstractmethod

class StorageBackend(ABC):
    @abstractmethod
    def save(self, data: dict):
        pass

    @abstractmethod
    def query_all(self) -> list:
        pass

    @abstractmethod
    def clear(self):
        pass
