build-docker:
	docker build -t pubmed-parser .

run-docker:
	docker run --rm -p 8000:8000 --dns=8.8.8.8 pubmed-parser

run-docker-volume:
	docker run --rm -v $(pwd):/app pubmed-parser

run-cli-json:
	python run.py --ids ids.txt --format json --file outputfce.json

run-cli-csv:
	python run.py --ids ids.txt --format csv --file outputfce.csv
