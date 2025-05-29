
import argparse
from pmc_api_client import PMCAPIClient
from pmc_parser import PMCParser
from csv_exporter import CSVExporter
from json_exporter import JSONExporter
from logger_config import setup_logger
from data_sources.factory import get_data_source
from config import LOG_LEVEL

logger = setup_logger("fce", level=LOG_LEVEL)
# logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Fetch and parse full-text research papers from PMC.')

    parser.add_argument('--ids', type=str, required=True,
                        help='File containing multiple PMCIDs (one per line)')
    parser.add_argument('--format', choices=['csv', 'json'],
                        help='Output file format')
    parser.add_argument('--file', type=str,
                        help='Output file name')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()

    if args.debug:
        logger.setLevel("DEBUG")
        logger.debug("Debug Mode ON")
    else:
        if not args.format or not args.file:
            parser.error("--format and --file are required unless --debug is used")

    client = PMCAPIClient()
    parser_ = PMCParser()

    # Read PMCIDs from file
    try:
        with open(args.ids, 'r') as f:
            pmcids = [line.strip() for line in f if line.strip()]
    except Exception as e:
        logger.error(f"Failed to read PMCIDs from file: {e}")
        return

    all_parsed_data = []
    source = get_data_source()
    # xml_data = source.fetch(pmcid)
    for pmcid in pmcids:
        logger.info(f"Processing {pmcid}...")
        # xml_data = client.fetch_pmc_article(pmcid)
        xml_data = source.fetch(pmcid)
        if not xml_data:
            logger.error(f"Failed to retrieve data from PMC for {pmcid}. Skipping.")
            continue
        parsed_data = parser_.parse(xml_data, pmcid)
        all_parsed_data.append(parsed_data)

    if not all_parsed_data:
        logger.error("No data was parsed successfully. Exiting.")
        return

    if args.debug:
        logger.debug(f"Parsed data: {all_parsed_data}")
    if args.format == 'csv':
        exporter = CSVExporter()
        exporter.save_to_csv_cli(all_parsed_data, args.file)
    elif args.format == 'json':
        exporter = JSONExporter()
        exporter.save_to_json(all_parsed_data, args.file)

    logger.info(f"Finished exporting data to {args.file}")

if __name__ == '__main__':
    main()

