f_id = "SN"
number = 1

student_list = []


def avg_score(math_score, physics_score, chemistry_score):
    return (math_score + physics_score + chemistry_score) / 3


def ranking(score):
    if score < 5:
        return "Yếu"
    elif score < 7:
        return "Trung bình"
    elif score < 8:
        return "Khá"
    else:
        return "Giỏi"


def add_student():
    global number

    student_id = f"{f_id}{number}"
    number += 1

    name = input("Nhập họ và tên sinh viên: ")

    math_score = float(input("Nhập điểm Toán: "))
    physics_score = float(input("Nhập điểm Lý: "))
    chemistry_score = float(input("Nhập điểm Hóa: "))

    average_score = avg_score(
        math_score,
        physics_score,
        chemistry_score,
    )

    new_student = {
        "id": student_id,
        "name": name,
        "math_score": math_score,
        "physics_score": physics_score,
        "chemistry_score": chemistry_score,
        "average_score": average_score,
        "ranking": ranking(average_score),
    }

    student_list.append(new_student)

    print("Thêm sinh viên thành công!")


def show_students():
    if len(student_list) == 0:
        print("Danh sách sinh viên trống!")
        return

    print("\nDANH SÁCH SINH VIÊN")

    for student in student_list:
        print("-" * 40)
        print(f"Mã SV: {student['id']}")
        print(f"Họ tên: {student['name']}")
        print(f"Toán: {student['math_score']}")
        print(f"Lý: {student['physics_score']}")
        print(f"Hóa: {student['chemistry_score']}")
        print(f"Điểm TB: {student['average_score']:.2f}")
        print(f"Xếp loại: {student['ranking']}")


def edit_score(student_id):
    for student in student_list:
        if student["id"] == student_id:
            math_score = float(input("Nhập điểm Toán mới: "))
            physics_score = float(input("Nhập điểm Lý mới: "))
            chemistry_score = float(input("Nhập điểm Hóa mới: "))

            average_score = avg_score(
                math_score,
                physics_score,
                chemistry_score,
            )

            student["math_score"] = math_score
            student["physics_score"] = physics_score
            student["chemistry_score"] = chemistry_score
            student["average_score"] = average_score
            student["ranking"] = ranking(average_score)

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sinh viên!")


def delete_student(student_id):
    for student in student_list:
        if student["id"] == student_id:
            student_list.remove(student)
            print("Xóa thành công!")
            return

    print("Không tìm thấy sinh viên!")


def search(student_id=None, name=None):
    results = []

    for student in student_list:
        if student_id is not None and student["id"] == student_id:
            results.append(student)

        elif (
            name is not None
            and name.lower() in student["name"].lower()
        ):
            results.append(student)

    return results


def statistical(rank_choice):
    rank_type = ""

    if rank_choice == 1:
        rank_type = "Giỏi"
    elif rank_choice == 2:
        rank_type = "Khá"
    elif rank_choice == 3:
        rank_type = "Trung bình"
    elif rank_choice == 4:
        rank_type = "Yếu"
    else:
        print("Lựa chọn không hợp lệ!")
        return

    count = 0

    for student in student_list:
        if student["ranking"] == rank_type:
            count += 1

    print(f"Số sinh viên loại {rank_type}: {count}")


while True:
    print("\n========== QUẢN LÝ SINH VIÊN ==========")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Sửa điểm sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Thống kê sinh viên")
    print("0. Thoát")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        student_id = input(
            "Nhập mã sinh viên cần sửa: "
        )
        edit_score(student_id)

    elif choice == "4":
        student_id = input(
            "Nhập mã sinh viên cần xóa: "
        )
        delete_student(student_id)

    elif choice == "5":
        print("1. Tìm theo ID")
        print("2. Tìm theo tên")

        search_choice = input("Chọn: ")

        if search_choice == "1":
            student_id = input("Nhập ID: ")
            results = search(student_id=student_id)

        elif search_choice == "2":
            name = input("Nhập tên: ")
            results = search(name=name)

        else:
            print("Lựa chọn không hợp lệ!")
            continue

        if len(results) == 0:
            print("Không tìm thấy sinh viên!")

        else:
            print("\nKẾT QUẢ TÌM KIẾM")

            for student in results:
                print("-" * 40)
                print(f"Mã SV: {student['id']}")
                print(f"Họ tên: {student['name']}")
                print(
                    f"Điểm TB: "
                    f"{student['average_score']:.2f}"
                )
                print(
                    f"Xếp loại: "
                    f"{student['ranking']}"
                )

    elif choice == "6":
        print("1. Giỏi")
        print("2. Khá")
        print("3. Trung bình")
        print("4. Yếu")

        rank_choice = int(
            input("Chọn loại cần thống kê: ")
        )

        statistical(rank_choice)

    elif choice == "0":
        print("Chương trình kết thúc!")
        break

    else:
        print("Lựa chọn không hợp lệ!")