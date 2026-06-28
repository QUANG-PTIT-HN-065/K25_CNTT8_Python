"""
1. Phân tích bài toán (I/O)

Input

name (chuỗi), bonus_atk (số), bonus_speed (số).
Thao tác lai tạo bằng toán tử + giữa hai đối tượng.

Output

Đối tượng sinh vật mới khi lai tạo thành công.
Thông báo khi sinh vật sử dụng kỹ năng.
Thông báo lỗi khi khởi tạo Companion hoặc lai tạo sai loại.

2. Đề xuất giải pháp (Architecture & Logic)

Sử dụng ABC và @abstractmethod cho lớp Companion để bắt buộc các lớp con phải cài đặt unleash_skill(), ngăn khởi tạo trực tiếp Companion.
Nạp chồng toán tử __add__, kiểm tra type(self) == type(other) để chỉ cho phép lai tạo giữa hai sinh vật cùng loại, nếu không sẽ phát sinh TypeError.
Lớp Dragon kế thừa Pet và Mount, sử dụng super() kết hợp **kwargs để khởi tạo đầy đủ bonus_atk và bonus_speed theo MRO.

3. Thiết kế các bước thực hiện

Bước 1: Import ABC và abstractmethod.
Bước 2: Tạo lớp Companion, viết __init__, __add__ và unleash_skill().
Bước 3: Tạo lớp Pet và Mount, kế thừa Companion, ghi đè unleash_skill().
Bước 4: Tạo lớp Dragon(Pet, Mount), khởi tạo bằng super() và ghi đè unleash_skill().
Bước 5: Viết if __name__ == "__main__": để kiểm thử các trường hợp theo yêu cầu.
"""

from model import Companion, Pet, Mount, Dragon


def main():
    print("===== TEST BẪY 1: KHỞI TẠO ABC =====")
    try:
        c = Companion("Test")
    except TypeError as e:
        print("Lỗi:", e)

    print("\n===== TẠO PET =====")
    p1 = Pet("Sói Trắng", bonus_atk=50)
    p2 = Pet("Sói Đen", bonus_atk=60)

    print(f"{p1.name} | Level: {p1.level} | Atk: {p1.bonus_atk}")
    print(f"{p2.name} | Level: {p2.level} | Atk: {p2.bonus_atk}")

    print("\n===== TEST LAI TẠO =====")
    p3 = p1 + p2

    print("Lai tạo thành công!")
    print(f"Tên: {p3.name}")
    print(f"Level: {p3.level}")
    print(f"Atk: {p3.bonus_atk}")

    print("\n===== TEST BẪY 2 =====")

    m1 = Mount("Ngựa", bonus_speed=10)

    try:
        p1 + m1
    except TypeError as e:
        print("Lỗi:", e)

    try:
        p1 + 10
    except TypeError as e:
        print("Lỗi:", e)

    print("\n===== TEST DRAGON =====")

    d1 = Dragon("Rồng Lửa", bonus_atk=500, bonus_speed=200)

    print(f"Tên: {d1.name}")
    print(f"Level: {d1.level}")
    print(f"Atk: {d1.bonus_atk}")
    print(f"Speed: {d1.bonus_speed}")

    print("\n===== TEST ĐA HÌNH =====")

    equipped = [p3, m1, d1]

    for companion in equipped:
        companion.unleash_skill()


main()
