# data_sources/factory.py

from config import DATA_SOURCE
from .pmc_source import PMCSource
# from .arxiv_source import ArxivSource  #example for future extension

def get_data_source():
    if DATA_SOURCE == "PMC":
        return PMCSource()
    # elif DATA_SOURCE == "ArXiv":
    #     return ArxivSource()
    else:
        raise ValueError(f"Unsupported data source: {DATA_SOURCE}")
