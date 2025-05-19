# Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Install ca-certificates and any other dependencies
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*


# Copy all your code into /app
COPY . .

# Install dependencies (adjust as needed)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port if your app serves something
# EXPOSE 8000

# Command to run your app
CMD ["python", "run.py", "--ids", "ids.txt", "--format", "json", "--file", "fce_output.json"]



