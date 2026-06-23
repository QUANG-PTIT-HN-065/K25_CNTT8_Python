"""
PHẦN 1: Phân tích thiết kế
Cấu trúc thư mục
rikkei_learning_tools/
├── main.py
├── data/
│   └── students.py
├── utils/
│   ├── __init__.py
│   ├── score_utils.py
│   ├── string_utils.py
│   └── random_utils.py
└── reports/
    ├── __init__.py
    └── report_generator.py

Module score_utils.py
- Vai trò: Xử lý điểm.
- Hàm: calculate_average(), classify_student()
- Import: import math

Module string_utils.py
- Vai trò: Chuẩn hóa tên sinh viên.
- Hàm: normalize_student_names()
- Import: không cần.

Module random_utils.py
- Vai trò: Sinh mã bài tập.
- Hàm: generate_assignment_code()
- Import: import random, import string as st

Module report_generator.py
- Vai trò: Hiển thị và xuất báo cáo.
- Hàm: display_student_scores(), export_learning_report()
- Import:
    + from utils.score_utils import calculate_average
    + from datetime import datetime
    + from colorama import Fore

Mô tả các hàm

| Hàm                              | Input | Output   |
| -------------------------------- | ----- | -------- |
| calculate_average(scores)        | list  | float    |
| classify_student(avg)            | float | str      |
| display_student_scores(records)  | list  | None     |
| normalize_student_names(records) | list  | None     |
| generate_assignment_code()       | None  | str      |
| export_learning_report(records)  | list  | file txt |
| main()                           | None  | Menu     |

"""

from data.students import student_records
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code
from reports.report_generator import display_student_scores, export_learning_report

while True:
    print("\n1. Xem điểm")
    print("2. Chuẩn hóa tên")
    print("3. Sinh mã bài tập")
    print("4. Xuất báo cáo")
    print("5. Thoát")

    try:
        choice = int(input("Chọn: "))
    except ValueError:
        print("Chức năng không hợp lệ.")
        continue

    if choice == 1:
        display_student_scores(student_records)

    elif choice == 2:
        normalize_student_names(student_records)

    elif choice == 3:
        print(generate_assignment_code())

    elif choice == 4:
        export_learning_report(student_records)

    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Chức năng không hợp lệ.")
