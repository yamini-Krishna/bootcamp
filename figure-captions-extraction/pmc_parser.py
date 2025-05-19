'''
import xml.etree.ElementTree as ET
from logger_config import setup_logger

from config import LOG_LEVEL

logger = setup_logger("pubtator_api", level=LOG_LEVEL)

class PMCParser:
    def parse(self, xml_data: str, pmcid: str) -> dict:
        logger.debug("Parsing PMC XML data.")
        try:
            root = ET.fromstring(xml_data)

            title_elem = root.find(".//article-title")
            title = ''.join(title_elem.itertext()).strip() if title_elem is not None else "No title found"

            abstract_elem = root.find(".//abstract")
            abstract = ''.join(abstract_elem.itertext()).strip() if abstract_elem is not None else "No abstract found"

            figures = []
            for fig in root.findall(".//fig"):
                fig_data = {}

                label_elem = fig.find("label")
                fig_data['label'] = label_elem.text.strip() if label_elem is not None and label_elem.text else "No label"

                caption_elem = fig.find("caption")
                fig_data['caption'] = ''.join(caption_elem.itertext()).strip() if caption_elem is not None else "No caption"

                graphic_elem = fig.find(".//graphic")
                if graphic_elem is not None:
                    href = graphic_elem.attrib.get("{http://www.w3.org/1999/xlink}href")
                    fig_data['image_url'] = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/bin/{href}" if href else "No image URL"
                else:
                    fig_data['image_url'] = "No image URL"

                fig_data['key_entities'] = ["GENE1", "GENE2"] 

                figures.append(fig_data)

            return {
                'PMCID': pmcid,
                'title': title,
                'abstract': abstract,
                'figures': figures
            }

        except Exception as e:
            logger.error(f"Error parsing XML: {e}")
            return {}
        '''
'''
import xml.etree.ElementTree as ET
from logger_config import setup_logger
from config import LOG_LEVEL

import requests
import time

logger = setup_logger("pubtator_api", level=LOG_LEVEL)
'''
'''
# === BERN2 Entity Extraction Helper ===
def fetch_entities_from_bern(caption: str, max_retries=3):
    if not caption or len(caption.strip()) < 20:
        return []

    url = "http://bern2.korea.ac.kr/plain"
    headers = {"Content-Type": "application/json"}
    payload = {"text": caption}

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            entities = []
            for ann in data.get("annotations", []):
                entity = {
                    "text": ann.get("mention", ""),
                    "type": ann.get("obj", "unknown"),
                    "identifier": ann.get("id", [None])[0],
                    "start": ann.get("span", {}).get("begin", 0),
                    "end": ann.get("span", {}).get("end", 0),
                }
                entities.append(entity)

            return entities

        except Exception as e:
            logger.warning(f"BERN2 request failed (attempt {attempt+1}): {e}")
            time.sleep(2 * (attempt + 1))  # Exponential backoff

    logger.error("BERN2 entity extraction failed after retries.")
    return []
'''
'''
# === Main PMCParser ===
class PMCParser:
    def parse(self, xml_data: str, pmcid: str) -> dict:
        logger.debug("Parsing PMC XML data.")
        try:
            root = ET.fromstring(xml_data)

            title_elem = root.find(".//article-title")
            title = ''.join(title_elem.itertext()).strip() if title_elem is not None else "No title found"

            abstract_elem = root.find(".//abstract")
            abstract = ''.join(abstract_elem.itertext()).strip() if abstract_elem is not None else "No abstract found"

            figures = []

            for fig in root.findall(".//fig"):
                fig_data = {}

                label_elem = fig.find("label")
                fig_data['label'] = label_elem.text.strip() if label_elem is not None and label_elem.text else "No label"
                logger.debug(f"Figure label: {fig_data['label']}")

                caption_elem = fig.find("caption")
                caption = ''.join(caption_elem.itertext()).strip() if caption_elem is not None else "No caption"
                fig_data['caption'] = caption
                logger.debug(f"Caption: {caption}")

                graphic_elem = fig.find(".//graphic")
                if graphic_elem is not None:
                    href = graphic_elem.attrib.get("{http://www.w3.org/1999/xlink}href")
                    fig_data['image_url'] = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/bin/{href}" if href else "No image URL"
                else:
                    fig_data['image_url'] = "No image URL"

                # Entity extraction
              #  entities = fetch_entities_from_bern(caption)
                fig_data['key_entities'] = ["GENE1", "GENE2"] 

              
                #logger.debug(f"Entities found: {entities}")

                figures.append(fig_data)

            return {
                'PMCID': pmcid,
                'title': title,
                'abstract': abstract,
                'figures': figures
            }

        except Exception as e:
            logger.error(f"Error parsing XML: {e}")
            return {}
'''
import xml.etree.ElementTree as ET
import logging
import requests
import time

from logger_config import setup_logger
from config import LOG_LEVEL, ENABLE_ENTITY_EXTRACTION

logger = setup_logger("pubtator_api", level=LOG_LEVEL)

def fetch_entities_from_bern(caption: str, max_retries=3) -> list:
    if not ENABLE_ENTITY_EXTRACTION:
        logger.debug("Entity extraction is disabled.")
        return []

    if not caption or len(caption) < 20:
        logger.debug("Caption too short or empty.")
        return []

    url = "http://bern2.korea.ac.kr/plain"
    payload = {"text": caption}
    headers = {"Content-Type": "application/json"}

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            entities = []

            for ann in data.get("annotations", []):
                entity = {
                    "text": ann.get("mention", ""),
                    "type": ann.get("obj", "unknown"),
                    "identifier": None,
                    "start": ann.get("span", {}).get("begin", 0),
                    "end": ann.get("span", {}).get("end", 0)
                }
                id_list = ann.get("id", [])
                if id_list:
                    entity["identifier"] = id_list[0]
                entities.append(entity)

            logger.info(f"Extracted {len(entities)} entities from caption.")
            return entities

        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(2 * (attempt + 1))  # Exponential backoff

    logger.error("All attempts to fetch entities from BERN2 failed.")
    return []


class PMCParser:
    def parse(self, xml_data: str, pmcid: str) -> dict:
        logger.debug("Parsing PMC XML data.")
        try:
            root = ET.fromstring(xml_data)

            title_elem = root.find(".//article-title")
            title = ''.join(title_elem.itertext()).strip() if title_elem is not None else "No title found"

            abstract_elem = root.find(".//abstract")
            abstract = ''.join(abstract_elem.itertext()).strip() if abstract_elem is not None else "No abstract found"

            figures = []
            for fig in root.findall(".//fig"):
                fig_data = {}

                label_elem = fig.find("label")
                fig_data['label'] = label_elem.text.strip() if label_elem is not None and label_elem.text else "No label"

                caption_elem = fig.find("caption")
                fig_data['caption'] = ''.join(caption_elem.itertext()).strip() if caption_elem is not None else "No caption"

                graphic_elem = fig.find(".//graphic")
                if graphic_elem is not None:
                    href = graphic_elem.attrib.get("{http://www.w3.org/1999/xlink}href")
                    fig_data['image_url'] = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/bin/{href}" if href else "No image URL"
                else:
                    fig_data['image_url'] = "No image URL"

                # Extract key entities from caption using BERN2
                fig_data['key_entities'] = fetch_entities_from_bern(fig_data['caption'])

                figures.append(fig_data)

            return {
                'PMCID': pmcid,
                'title': title,
                'abstract': abstract,
                'figures': figures
            }

        except Exception as e:
            logger.error(f"Error parsing XML: {e}")
            return {}
