import requests
from logger_config import setup_logger
from config import LOG_LEVEL

logger = setup_logger("pubtator_api", level=LOG_LEVEL)

class PMCAPIClient:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def fetch_pmc_article(self, pmcid: str) -> str:
   
        logger.debug(f"Fetching full-text XML for PMCID: {pmcid}")
        try:
            params = {
                'db': 'pmc',
                'id': pmcid,
                'retmode': 'xml'
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            logger.debug("Successfully fetched XML data.")
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching PMC article {pmcid}: {e}")
            return None
