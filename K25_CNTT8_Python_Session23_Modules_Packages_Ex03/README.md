Rikkei_Aviation/
│
├── main.py
├── core/
│   ├── __init__.py
│   ├── logistics.py
│   └── manager.py
├── utils/
│   ├── __init__.py
│   ├── time_helper.py
│   └── file_helper.py
└── aviation_logs/

Tại sao không nên dùng from math import *
Gây ô nhiễm không gian tên.
Dễ xảy ra xung đột tên hàm, biến.
Khó bảo trì và đọc mã nguồn.

Nên dùng:

import math

hoặc

from math import ceil