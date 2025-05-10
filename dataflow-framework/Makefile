# Define variables
PROJECT_NAME = dataflow-framework
DOCKER_IMAGE = dataflow-framework:latest
DOCKER_COMPOSE_FILE = docker-compose.yml
PYTHON_ENV = venv
MAIN_FILE = main.py
WATCH_DIR = watch_dir

# Command to start the FastAPI server
RUN_SERVER = uvicorn ${MAIN_FILE}:app --host 0.0.0.0 --port 8000 --reload

# Help command to display available tasks
help:
	@echo "Makefile for ${PROJECT_NAME}"
	@echo ""
	@echo "Available commands:"
	@echo "  make build-docker     Build Docker image"
	@echo "  make run              Run the application in single file mode"
	@echo "  make watch            Run the application in watch mode"
	@echo "  make test             Run tests (if any)"
	@echo "  make clean            Clean the project (remove .pyc files)"
	@echo "  make install          Install dependencies"
	@echo "  make docker-up        Start Docker containers"
	@echo "  make docker-down      Stop Docker containers"

# Install Python dependencies in the virtual environment
install:
	python3 -m venv $(PYTHON_ENV)
	$(PYTHON_ENV)/bin/pip install -r requirements.txt

# Run the application in single file mode
run: 
	@echo "Running in single file mode..."
	python $(MAIN_FILE) --input $(WATCH_DIR)/sample_log_01.txt

# Run the application in watch mode
watch:
	@echo "Running in watch mode..."
	python $(MAIN_FILE) --watch

# Build the Docker image
build-docker:
	docker build -t $(DOCKER_IMAGE) .

# Start Docker containers (for example, if you have a database or additional services)
docker-up:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

# Stop Docker containers
docker-down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

# Clean Python bytecode files
clean:
	@echo "Cleaning Python bytecode files..."
	find . -name "*.pyc" -exec rm -f {} \;

# Run tests (if you have any tests in your project)
test:
	@echo "Running tests..."
	pytest

# Run server locally (FastAPI)
run-server:
	@echo "Starting FastAPI server..."
	$(RUN_SERVER)

# Publish Docker image to a Docker registry
publish-docker:
	docker push $(DOCKER_IMAGE)

# Remove Docker images
clean-docker:
	docker rmi $(DOCKER_IMAGE)
