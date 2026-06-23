"""
PHẦN 1: PHÂN TÍCH VÀ TÁI CẤU TRÚC
1. Vì sao from math import * là Anti-pattern?
Gây ô nhiễm không gian tên (namespace).
Dễ xảy ra xung đột tên hàm, khó bảo trì.
Khó biết hàm nào đến từ thư viện nào.

Cách import an toàn:

import math

hoặc:

from math import radians, sin, cos, sqrt, atan2
2. Tệp đặc biệt để tạo Package

Tệp cần có:

__init__.py

Vai trò:

Đánh dấu thư mục là một Package Python.
Cho phép import module từ thư mục đó.
Hỗ trợ quản lý và tổ chức mã nguồn.
3. Cấu trúc thư mục sau khi tối ưu
Rikkei_Logistics/
│
├── main.py
│
├── core/
│   ├── __init__.py
│   ├── geo_calculator.py
│   └── time_estimator.py
│
├── utils/
│   ├── __init__.py
│   └── file_helper.py
│
└── logs/
"""

from datetime import datetime
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00",
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00",
    },
]

print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

create_log_dir("logs")
print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
print("-" * 70)

for s in shipments:
    distance = calculate_distance(
        s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"]
    )

    eta = predict_eta(s["depart"], distance)

    deadline = datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")

    print(f"[CHUYẾN XE {s['id']}]")
    print(f"+ Khoảng cách vận chuyển: {distance:.2f} km")
    print(f"+ Thời gian khởi hành: {s['depart']}")
    print(f"+ Dự kiến cập bến (ETA): {eta}")

    if eta <= deadline:
        print("+ Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)")
    else:
        print(
            f"+ Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline.time()})"
        )

    print()
