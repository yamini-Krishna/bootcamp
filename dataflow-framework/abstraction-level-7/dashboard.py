from fastapi import FastAPI
from fastapi.responses import JSONResponse
from metrics import metrics_store, trace_store, errors_store
import threading
import time

app = FastAPI()

@app.get("/stats")
async def get_stats():
    """Return live processor metrics."""
    return JSONResponse(content=metrics_store)

@app.get("/trace")
async def get_trace():
    """Return recent line traces."""
    return JSONResponse(content=trace_store[-1000:])  # Last 1000 traces

@app.get("/errors")
async def get_errors():
    """Return recent processor-level errors."""
    return JSONResponse(content=errors_store[-1000:])  # Last 1000 errors

def start_dashboard():
    """Run the FastAPI server in a separate thread."""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", workers=1)

# Run the dashboard in the background
dashboard_thread = threading.Thread(target=start_dashboard)
dashboard_thread.daemon = True
dashboard_thread.start()
