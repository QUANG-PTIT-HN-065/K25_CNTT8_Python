# 1) Phân tích và thiết kế giải pháp
# Input
# Lựa chọn menu chính (int)
# Lựa chọn menu phụ (int)
# Tên bài hát (str)
# Vị trí chèn/xóa (int)

# Output
# Danh sách bài hát hiện tại
# Thông báo thêm, xóa, sắp xếp thành công
# 3 bài hát đầu tiên của playlist
# Thông báo lỗi khi dữ liệu không hợp lệ

# Đề xuất giải pháp
# Chức năng 1: Thêm bài hát
# Sử dụng append() để thêm cuối danh sách.
# Sử dụng insert(index, value) để chèn vào vị trí chỉ định.
# Kiểm tra vị trí hợp lệ trước khi chèn.
# Chức năng 2: Xem danh sách phát
# Dùng for kết hợp enumerate().
# Hiển thị STT bắt đầu từ 1.
# Nếu danh sách rỗng -> thông báo lỗi.
# Chức năng 3: Xóa bài hát
# Xóa theo tên: dùng remove().
# Xóa theo vị trí: dùng pop(index).
# Kiểm tra tên hoặc vị trí tồn tại trước khi xóa.
# Chức năng 4: Sắp xếp và trích xuất
# Sắp xếp tăng dần: sort()
# Sắp xếp giảm dần: sort(reverse=True)
# Lấy 3 bài đầu: slicing playlist[:3]
# Chức năng 5: Thoát
# Dùng break.
# Pseudocode
# Khởi tạo playlist rỗng

# Lặp vô hạn:
#     Hiển thị menu chính
#     Nhập lựa chọn
#     Nếu chọn 1:
#         Hiển thị menu thêm
#         Nếu thêm cuối:
#             Nhập tên bài hát
#             append()
#         Nếu chèn vị trí:
#             Nhập tên bài hát
#             Nhập vị trí
#             Kiểm tra vị trí hợp lệ
#             insert()
#     Nếu chọn 2:
#         Nếu playlist rỗng:
#             Thông báo
#         Ngược lại:
#             Hiển thị playlist
#     Nếu chọn 3:
#         Nếu playlist rỗng:
#             Thông báo
#         Hiển thị menu xóa
#         Nếu xóa theo tên:
#             remove()
#         Nếu xóa theo vị trí:
#             pop()
#     Nếu chọn 4:
#         Nếu playlist rỗng:
#             Thông báo

#         Hiển thị menu sắp xếp
#         Thực hiện chức năng tương ứng
#     Nếu chọn 5:
#         Kết thúc chương trình
#     Ngược lại:
#         Báo lỗi lựa chọn

playlist = []


def input_integer(message):
    while True:
        value = input(message).strip()

        try:
            return int(value)
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")


while True:
    print("\n===== MENU QUẢN LÝ DANH SÁCH PHÁT =====")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")

    choice = input_integer("Nhập lựa chọn của bạn: ")

    # Chức năng 1
    if choice == 1:
        print("\n----- THÊM BÀI HÁT -----")
        print("1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí bất kỳ")

        sub_choice = input_integer("Lựa chọn của bạn: ")

        if sub_choice == 1:
            song_name = input("Nhập tên bài hát: ").strip()

            playlist.append(song_name)

            print("Thêm bài hát thành công.")
            print(f"Số lượng bài hát hiện tại: {len(playlist)}")

        elif sub_choice == 2:
            song_name = input("Nhập tên bài hát: ").strip()
            position = input_integer("Nhập vị trí muốn chèn: ")

            if position < 1 or position > len(playlist) + 1:
                print("Vị trí không hợp lệ.")
            else:
                playlist.insert(position - 1, song_name)

                print("Thêm bài hát thành công.")
                print(f"Số lượng bài hát hiện tại: {len(playlist)}")

        else:
            print("Lựa chọn không hợp lệ.")

    # Chức năng 2
    elif choice == 2:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
        else:
            print("\n===== DANH SÁCH PHÁT =====")

            for index, song in enumerate(playlist, start=1):
                print(f"{index}. {song}")

    # Chức năng 3
    elif choice == 3:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n----- XÓA BÀI HÁT -----")
        print("1. Xóa theo tên")
        print("2. Xóa theo vị trí")

        sub_choice = input_integer("Lựa chọn của bạn: ")

        if sub_choice == 1:
            song_name = input("Nhập tên bài hát cần xóa: ").strip()

            if song_name in playlist:
                playlist.remove(song_name)
                print(f"Đã xóa bài hát {song_name} khỏi danh sách.")
            else:
                print("Không tìm thấy bài hát trong danh sách phát.")

        elif sub_choice == 2:
            position = input_integer("Nhập vị trí cần xóa: ")

            if position < 1 or position > len(playlist):
                print("Vị trí không hợp lệ.")
            else:
                deleted_song = playlist.pop(position - 1)
                print(f"Đã xóa bài hát {deleted_song} khỏi danh sách.")

        else:
            print("Lựa chọn không hợp lệ.")

    # Chức năng 4
    elif choice == 4:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n----- SẮP XẾP VÀ TRÍCH XUẤT -----")
        print("1. Sắp xếp A -> Z")
        print("2. Sắp xếp Z -> A")
        print("3. Nghe thử 3 bài hát đầu tiên")

        sub_choice = input_integer("Lựa chọn của bạn: ")

        if sub_choice == 1:
            playlist.sort()

            print("Danh sách sau khi sắp xếp:")
            for index, song in enumerate(playlist, start=1):
                print(f"{index}. {song}")

        elif sub_choice == 2:
            playlist.sort(reverse=True)

            print("Danh sách sau khi sắp xếp:")
            for index, song in enumerate(playlist, start=1):
                print(f"{index}. {song}")

        elif sub_choice == 3:
            print("\n===== 3 BÀI HÁT ĐẦU TIÊN =====")

            for index, song in enumerate(playlist[:3], start=1):
                print(f"{index}. {song}")

        else:
            print("Lựa chọn không hợp lệ.")

    # Chức năng 5
    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    # Menu sai
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")