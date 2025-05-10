#!/bin/bash

echo "Installing requirements..."
pip install -r requirements.txt

echo "Starting system in watch mode..."
python main.py --watch --trace
