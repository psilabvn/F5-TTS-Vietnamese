#!/bin/bash
# Start FastAPI server

# Activate virtual environment
source /home/psilab/F5-TTS-Vietnamese/venv/bin/activate

export HF_HOME="/home/psilab/.cache/huggingface"
export HF_HUB_CACHE="/home/psilab/.cache/huggingface/hub"

echo "API will be available at: http://localhost:8000"
echo "API docs available at: http://localhost:8000/docs"

cd "$(dirname "$0")"
python main.py
