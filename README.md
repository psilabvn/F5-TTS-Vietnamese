# F5-TTS-Vietnamese

Hệ điều hành: Ubuntu

## Các bước cài đặt

### 1. Tạo môi trường ảo
```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 2. Cài đặt PyTorch
```bash
pip install torch==2.4.0+cu124 torchaudio==2.4.0+cu124 --extra-index-url https://download.pytorch.org/whl/cu124
```

### 3. Cài đặt các thư viện khác
```bash
pip install f5-tts
pip install .
```

### 4. Tải model đã được fine-tune tiếng Việt
- Tải 2 file `model_last.pt` và `vocab.txt` từ: https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice/tree/main
- Đặt vào folder `model/`
- **Lưu ý:** Đổi tên file `config.json` thành `vocab.txt`

## Hướng dẫn sử dụng

### Yêu cầu đầu vào text
Để có kết quả tốt nhất, văn bản đầu vào cần:
- Loại bỏ ký tự đặc biệt
- Thay số bằng chữ (ví dụ: `1` → `một`)
- Thay dấu `.` bằng `,`
- Chuyển tất cả chữ hoa thành chữ thường

### Tài nguyên có sẵn
- **Reference voices**: Folder `original_voice_ref/` chứa các giọng mẫu (Khá Bảnh, Trần Hà Linh, Thời sự, Phim tài liệu, ...)
- **Scripts inference**: Folder `script_infer/` chứa các script chạy mẫu
- **Output**: Kết quả sau khi chạy sẽ được lưu vào folder `output/`

### API Server
Folder `fast_api/` chứa script để tạo API cho server
