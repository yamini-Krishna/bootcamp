from fastapi import FastAPI
from fastapi.responses import JSONResponse
import threading
import time
import uvicorn
from metrics import Metrics

# Create an instance of Metrics
metrics = Metrics()

# FastAPI app setup
app = FastAPI()

# Root endpoint to fix the 404 error
@app.get("/")
async def root():
    return {"message": "Welcome to the Metrics Dashboard! Visit /stats, /trace, or /errors for more info."}

# This function will start the FastAPI server in a separate thread
def start_server():
    try:
        print("Starting FastAPI server...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f"Error starting FastAPI server: {e}")

# Start the FastAPI server in a separate thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

@app.get("/stats")
async def get_stats():
    print("Fetching stats...")
    return JSONResponse({
        "total_lines_processed": metrics.total_lines_processed,
        "total_processing_time": metrics.total_processing_time,
        "total_errors": metrics.total_errors,
        "lines_processed_by_each_processor": metrics.lines_processed_by_each_processor
    })

@app.get("/trace")
async def get_trace():
    print("Fetching trace...")
    return JSONResponse({"recent_traces": metrics.recent_traces})

@app.get("/errors")
async def get_errors():
    print("Fetching errors...")
    return JSONResponse({"recent_errors": metrics.recent_errors})

# Simulate processing function
def process_line(line):
    processor_name = "general"
    start_time = time.time()

    time.sleep(0.1)
    
    processing_time = time.time() - start_time
    metrics.update_processor_count(processor_name)
    metrics.update_processing_time(processing_time)

    if "error" in line:
        metrics.update_error_count()

    metrics.add_trace(processor_name)

# Start processing sample lines for testing
process_line("error: This is an error message")
process_line("warn: This is a warning message")
process_line("general: This is a general message")

# Ensure main thread stays alive
print("Server is running in the background, you can visit http://localhost:8000")
while True:
    time.sleep(1)
