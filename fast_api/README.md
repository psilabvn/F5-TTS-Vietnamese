# F5-TTS FastAPI Server

Simple FastAPI server for Vietnamese text-to-speech synthesis.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Start the server

```bash
python main.py
```

Or with uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API Endpoints

#### 1. Get available voices
```bash
curl http://localhost:8000/voices
```

#### 2. Synthesize speech
```bash
curl -X POST http://localhost:8000/synthesize \
  -H "Content-Type: application/json" \
  -d '{
    "voice": "tran_ha_linh",
    "text": "xin chào các bạn, hôm nay tôi sẽ chia sẻ về công nghệ",
    "speed": 1.0,
    "output_file": "test_output.wav"
  }'
```

#### 3. View API documentation
Open browser: `http://localhost:8000/docs`

## Example with Python

```python
import requests

response = requests.post(
    "http://localhost:8000/synthesize",
    json={
        "voice": "tran_ha_linh",
        "text": "đây là một ví dụ về tổng hợp giọng nói",
        "speed": 1.0,
        "output_file": "my_output.wav"
    }
)

print(response.json())
```

## Available Voices

- tran_ha_linh
- kha_banh
- chi_hang

(Add more voices in `main.py` VOICES dictionary)
