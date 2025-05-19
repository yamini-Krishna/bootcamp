import json
import logging
from config import LOG_LEVEL
from logger_config import setup_logger

logger = setup_logger("pubtator_api", level=LOG_LEVEL)
# logger = logging.getLogger(__name__)

class JSONExporter:
    def __init__(self):
        pass

    def save_to_json(self, data, filename):
        """
        Save a list of parsed data dictionaries to a JSON file.

        Args:
            data (list): List of parsed data dictionaries.
            filename (str): Output JSON filename.

        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            logger.info(f"Data successfully saved to JSON file: {filename}")
            return True
        except (IOError, TypeError) as e:
            logger.error(f"Failed to save data to JSON file '{filename}': {e}")
            return False
