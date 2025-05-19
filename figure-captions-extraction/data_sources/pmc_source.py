# data_sources/pmc_source.py

from pmc_api_client import PMCAPIClient
from .base import DataSource

class PMCSource(DataSource):
    def __init__(self):
        self.client = PMCAPIClient()

    def fetch(self, pmcid: str) -> str:
        return self.client.fetch_pmc_article(pmcid)
