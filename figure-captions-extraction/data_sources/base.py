# data_sources/base.py

from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def fetch(self, pmcid: str) -> str:
        """Fetch raw data (e.g., XML) for a given PMCID or identifier"""
        pass
