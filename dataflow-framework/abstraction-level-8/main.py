import os
import shutil
import time
import threading
import argparse
from processor import process_file
from dashboard import start_dashboard, metrics
import shutil

from utils import metrics


WATCH_DIR = "watch_dir"
UNPROCESSED = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS = os.path.join(WATCH_DIR, "underprocess")
PROCESSED = os.path.join(WATCH_DIR, "processed")


def recover_files():
    # Recover files from UNDERPROCESS back to UNPROCESSED
    for f in os.listdir(UNDERPROCESS):
        src = os.path.join(UNDERPROCESS, f)
        dst = os.path.join(UNPROCESSED, f)
        shutil.move(src, dst)
        print(f"[Recovery] Moved {f} back to unprocessed.")


def monitor_folder(trace_enabled):
    while True:
        files = sorted(os.listdir(UNPROCESSED))
        if files:
            filename = files[0]
            src = os.path.join(UNPROCESSED, filename)
            dst = os.path.join(UNDERPROCESS, filename)
            shutil.move(src, dst)
            print(f"[Monitor] Processing {filename}")
            metrics['current_file'] = filename
            process_file(dst, trace_enabled)
            shutil.move(dst, os.path.join(PROCESSED, filename))
            metrics['last_processed'].append(filename)
            metrics['current_file'] = None
        else:
            # Instead of continuously printing, wait for a short period before checking again
            print("No files to process, waiting...")
            time.sleep(2)  # Adjust the delay as needed





def start_dashboard_thread():
    # Start the FastAPI dashboard in a separate thread
    threading.Thread(target=start_dashboard, daemon=True).start()


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="Watch mode")
    parser.add_argument("--input", type=str, help="Single file mode")
    parser.add_argument("--trace", action="store_true", help="Enable trace logging")
    args = parser.parse_args()

    # Start the dashboard in a separate thread
    start_dashboard_thread()

    if args.input:
        # Process a single file
        process_file(args.input, args.trace)
    elif args.watch:
        # In watch mode, recover files and monitor the folder
        recover_files()
        monitor_folder(args.trace)
