from utils.score_utils import calculate_average, classify_student
from datetime import datetime
from colorama import Fore


def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    for student in records:
        avg = calculate_average(student["scores"])
        rank = classify_student(avg)
        print(f'[{student["student_id"]}] {student["name"]} | ĐTB: {avg:.2f} - {rank}')


def export_learning_report(records):
    total = len(records)
    passed = 0

    for student in records:
        if calculate_average(student["scores"]) >= 5:
            passed += 1

    failed = total - passed

    with open("learning_report.txt", "w", encoding="utf-8") as file:
        file.write(f"Thời gian: {datetime.now()}\n")
        file.write(f"Tổng sinh viên: {total}\n")
        file.write(f"Đạt: {passed}\n")
        file.write(f"Cần cải thiện: {failed}")

    print(Fore.GREEN + "Đã xuất báo cáo thành công!")
