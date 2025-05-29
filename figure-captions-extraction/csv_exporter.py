
import csv
import json
from logger_config import setup_logger
from config import LOG_LEVEL

logger = setup_logger("pubtator_api", level=LOG_LEVEL)

class CSVExporter:
    def save_to_csv_cli(self, data, filename):
        logger.debug(f"Saving data to CSV file: {filename}")
        try:
            fieldnames = [
                "PMCID", "title", "abstract", "figure_label", "figure_caption", "figure_image_url", "figure_key_entities"
            ]

            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for item in data:
                    pmcid = item.get("PMCID", "")
                    title = item.get("title", "")
                    abstract = item.get("abstract", "")
                    figures = item.get("figures", [])

                    if figures:
                        for fig in figures:
                            writer.writerow({
                                "PMCID": pmcid,
                                "title": title,
                                "abstract": abstract,
                                "figure_label": fig.get("label", ""),
                                "figure_caption": fig.get("caption", ""),
                                "figure_image_url": fig.get("image_url", ""),
                                "figure_key_entities": ", ".join(
                                    f"{ent.get('text')} ({ent.get('type')})"
                                    for ent in fig.get("key_entities", [])
                                )
                            })
                    else:
                        writer.writerow({
                            "PMCID": pmcid,
                            "title": title,
                            "abstract": abstract,
                            "figure_label": "",
                            "figure_caption": "",
                            "figure_image_url": "",
                            "figure_key_entities": ""
                        })

            logger.info(f"Results successfully saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")

    def save_to_csv_api(self, data: list[dict], filename: str):
        if not data:
            logger.warning("No data provided to save_to_csv_api")
            return

        fieldnames = list(data[0].keys())

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for row in data:
                    flat_row = {
                        key: json.dumps(value) if isinstance(value, (list, dict)) else value
                        for key, value in row.items()
                    }
                    writer.writerow(flat_row)
            logger.info(f"API results successfully saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving API data to CSV: {e}")
