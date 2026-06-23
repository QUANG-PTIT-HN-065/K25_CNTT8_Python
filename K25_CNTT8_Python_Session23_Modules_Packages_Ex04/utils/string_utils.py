def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    for student in records:
        student["name"] = " ".join(student["name"].split()).title()
        print(f'{student["student_id"]}: {student["name"]}')
