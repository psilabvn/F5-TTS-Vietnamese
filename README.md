# F5-TTS-Vietnamese

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.4.0-red.svg)](https://pytorch.org/)

*Text-to-Speech chất lượng cao cho tiếng Việt*

</div>

---

## 📖 Giới thiệu

**F5-TTS-Vietnamese** là một hệ thống Text-to-Speech (TTS) tiên tiến cho tiếng Việt, được xây dựng dựa trên mô hình [F5-TTS](https://github.com/SWivid/F5-TTS) và sử dụng mô hình đã được fine-tune tiếng Việt của [hynt](https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice).

### ✨ Tính năng nổi bật

- 🎭 **10+ giọng nói chất lượng cao**: Bao gồm giọng của các nhân vật nổi tiếng, phát thanh viên thời sự, giọng đọc phim tài liệu, v.v.
- 🚀 **Sẵn sàng sử dụng**: Script đã được cấu hình và tối ưu, có thể chạy ngay lập tức
- 🔧 **Dễ dàng tùy chỉnh**: Hỗ trợ thêm giọng nói mới và điều chỉnh theo nhu cầu
- 🌐 **API Server**: Tích hợp FastAPI để dễ dàng triển khai dịch vụ TTS
- 💯 **Chất lượng cao**: Giọng nói tự nhiên, cảm xúc phong phú

### 🖥️ Yêu cầu hệ thống

- **Hệ điều hành**: Ubuntu (hoặc các bản phân phối Linux khác)
- **Python**: 3.10
- **CUDA**: 12.4 (khuyến nghị cho GPU acceleration)
- **RAM**: Tối thiểu 8GB
- **GPU**: NVIDIA GPU với ít nhất 6GB VRAM (khuyến nghị)

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
