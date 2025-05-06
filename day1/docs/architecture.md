# Architecture Overview

## Components
- **Camera Input**: Captures gesture
- **Frontend (Streamlit)**: Shows UI and output
- **Backend (Python)**: Handles prediction logic
- **CNN Model**: Classifies gestures
- **Database (optional)**: Logs gesture results

## Data Flow
1. User shows a gesture to the camera
2. Frame is captured and sent to backend
3. Backend runs model → label returned
4. Label shown on screen (and optionally stored)

## Key Constraints
- Model input: grayscale 48x48px images
- Model must infer < 1s per gesture
