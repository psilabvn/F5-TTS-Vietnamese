#!/usr/bin/env python3
"""
Simple FastAPI server for F5-TTS Vietnamese inference
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
from pathlib import Path
import os

app = FastAPI(title="F5-TTS Vietnamese API")

# Set HuggingFace cache
os.environ["HF_HOME"] = "/home/psilab/.cache/huggingface"
os.environ["HF_HUB_CACHE"] = "/home/psilab/.cache/huggingface/hub"

# Base paths
BASE_DIR = Path(__file__).parent.parent
REF_AUDIO_DIR = BASE_DIR / "original_voice_ref"
OUTPUT_DIR = BASE_DIR / "output"

# Available voices
VOICES = {
    "tran_ha_linh": {
        "audio": "tran_ha_linh/tran_ha_linh_trimmed.wav",
        "ref_text": "công khai điểm luôn, hồi đó là toán tám phẩy năm, văn sau phẩy năm, tiếng anh chín phẩy bao nhiêu ấy, còn lịch sử cũng chín phẩy bao nhiêu luôn, được chưa, vô đê lên coi, có bảng điểm trên thớt đó"
    },
    "kha_banh": {
        "audio": "kha_banh/kha_banh_trimmed.wav",
        "ref_text": "example reference text for kha banh"
    },
    "chi_hang": {
        "audio": "chi_hang/chi_hang_trimmed.wav",
        "ref_text": "example reference text for chi hang"
    }
}


class TTSRequest(BaseModel):
    voice: str = "tran_ha_linh"
    text: str
    speed: float = 1.0
    output_file: str = "output.wav"


@app.get("/")
def read_root():
    return {
        "message": "F5-TTS Vietnamese API",
        "available_voices": list(VOICES.keys())
    }


@app.get("/voices")
def list_voices():
    """Get list of available voices"""
    return {"voices": list(VOICES.keys())}


@app.post("/synthesize")
def synthesize(request: TTSRequest):
    """
    Synthesize speech from text
    
    Example:
    {
        "voice": "tran_ha_linh",
        "text": "xin chào các bạn",
        "speed": 1.0,
        "output_file": "output.wav"
    }
    """
    # Validate voice
    if request.voice not in VOICES:
        raise HTTPException(
            status_code=400,
            detail=f"Voice '{request.voice}' not found. Available: {list(VOICES.keys())}"
        )
    
    # Get voice config
    voice_config = VOICES[request.voice]
    ref_audio = REF_AUDIO_DIR / voice_config["audio"]
    
    # Check if reference audio exists
    if not ref_audio.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Reference audio not found: {ref_audio}"
        )
    
    # Prepare output
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / request.output_file
    
    # Build command
    command = [
        "f5-tts_infer-cli",
        "--model", "F5TTS_Base",
        "--ref_audio", str(ref_audio),
        "--ref_text", voice_config["ref_text"],
        "--gen_text", request.text,
        "--speed", str(request.speed),
        "--vocoder_name", "vocos",
        "--vocab_file", str(BASE_DIR / "model/vocab.txt"),
        "--ckpt_file", str(BASE_DIR / "model/model_last.pt"),
        "--output_dir", str(OUTPUT_DIR),
        "--output_file", request.output_file
    ]
    
    try:
        # Run inference
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        
        return {
            "status": "success",
            "voice": request.voice,
            "text": request.text,
            "output_file": str(output_path),
            "message": "Speech synthesized successfully"
        }
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Inference failed: {e.stderr}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
