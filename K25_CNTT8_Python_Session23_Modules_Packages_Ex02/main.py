"""
PHẦN 1: Phân tích và Thiết kế Kiến trúc
1. Tác hại của from datetime import *
Gây ô nhiễm không gian tên, dễ xung đột biến và hàm.
Khó bảo trì, khó biết đối tượng nào thuộc thư viện nào.
Nếu có biến time = 120, việc import * có thể gây nhầm lẫn với lớp/hàm time của thư viện datetime.

Import an toàn:

import datetime

hoặc

from datetime import datetime
2. Hàm thay thế os.mkdir()

Sử dụng:

os.makedirs(path, exist_ok=True)
Tạo được thư mục lồng nhau.
Không gây lỗi nếu thư mục đã tồn tại.
3. Cấu trúc thư mục
Rikkei_Media/
│
├── main.py
│
├── storage/
│   ├── __init__.py
│   ├── disk_manager.py
│   └── io_helper.py
│
├── analytics/
│   ├── __init__.py
│   └── time_validator.py
│
└── media_vault/
"""

from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10",
    },
    {
        "filename": "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31",
    },
    {
        "filename": "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15",
    },
]

safe_create_dir("media_vault")

for media_file in raw_files:
    upload_date = parse_and_inspect_date(media_file["upload_at"])

    if upload_date is None:
        print(f"{media_file['filename']}: Lỗi ngày upload")
        continue

    blocks = calculate_disk_blocks(media_file["size_bytes"])

    folder = "audio" if media_file["filename"].endswith(".mp3") else "video"

    print(f"{media_file['filename']}")
    print(f"Blocks: {blocks}")
    print(f"Lưu vào thư mục: {folder}")
