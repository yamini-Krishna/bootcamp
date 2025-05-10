from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from utils import metrics


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the dashboard!"}




@app.get("/stats")
def get_stats():
    return JSONResponse({
        "total_lines_processed": metrics["total_lines_processed"],
        "total_processing_time": metrics["total_processing_time"],
        "total_errors": metrics["total_errors"],
        "lines_processed_by_each_processor": dict(metrics["lines_processed_by_each_processor"]),
        "current_file": metrics["current_file"],
        "last_processed_files": list(metrics["last_processed"])
    })

@app.get("/trace")
def get_trace():
    return JSONResponse({"recent_traces": list(metrics["trace"])})

@app.get("/errors")
def get_errors():
    return JSONResponse({"recent_errors": list(metrics["errors"])})

def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8000)
