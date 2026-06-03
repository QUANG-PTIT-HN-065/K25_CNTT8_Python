# 1. Phân tích và thiết kế
# Input

# menu_choice: int
# account_name: str
# video_title: str
# video_description: str
# hashtags: str
# keyword_find: str
# keyword_replace: str

# Output

# Thông tin video đã chuẩn hóa
# Thống kê độ dài mô tả, số từ, số hashtag
# Kết quả chuẩn hóa tài khoản
# Kết quả kiểm tra hashtag
# Kết quả tìm kiếm/thay thế từ khóa
# Giải pháp
# Dùng strip() loại bỏ khoảng trắng.
# Dùng title() chuẩn hóa tiêu đề.
# Dùng lower() và upper() chuyển đổi chữ.
# Dùng split() đếm từ.
# Dùng split(",") xử lý hashtag.
# Dùng replace() thay thế từ khóa.
# Dùng startswith() kiểm tra hashtag.
# Dùng vòng lặp while True để hiển thị menu.
# Dùng try-except kiểm tra lựa chọn menu.

# Pseudocode
# Lặp vô hạn
#     Hiển thị menu
#     Nhập lựa chọn

#     Nếu lựa chọn = 1
#         Nhập thông tin video
#         Kiểm tra dữ liệu hợp lệ
#         Hiển thị thống kê

#     Nếu lựa chọn = 2
#         Chuẩn hóa tên tài khoản

#     Nếu lựa chọn = 3
#         Kiểm tra hashtag hợp lệ
#         Nếu hợp lệ thêm vào danh sách hashtag

#     Nếu lựa chọn = 4
#         Tìm kiếm và thay thế từ khóa trong mô tả

#     Nếu lựa chọn = 5
#         Thoát chương trình

#     Ngược lại
#         Báo lỗi

video_description = ""
hashtag_list = []

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK ===")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra tính hợp lệ của hashtag")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")

    try:
        menu_choice = int(input("Mời bạn chọn chức năng (1-5): "))

        if menu_choice < 1 or menu_choice > 5:
            print("Lựa chọn không hợp lệ!")
            continue

    except ValueError:
        print("Lựa chọn không hợp lệ!")
        continue

    # Chức năng 1
    if menu_choice == 1:
        account_name = input("Nhập tên tài khoản: ")

        if account_name.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        video_title = input("Nhập tiêu đề video: ")
        video_description = input("Nhập mô tả video: ")

        if video_description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        hashtags = input("Nhập hashtag (cách nhau bởi dấu phẩy): ")

        hashtag_list = [tag.strip() for tag in hashtags.split(",") if tag.strip() != ""]

        print("\n===== BÁO CÁO =====")
        print("Tài khoản:", account_name.strip())
        print("Tiêu đề:", video_title.strip().title())
        print("Mô tả:", video_description.strip())
        print("Độ dài mô tả:", len(video_description.strip()))
        print("Số từ:", len(video_description.strip().split()))
        print("Danh sách hashtag:", hashtag_list)
        print("Số hashtag:", len(hashtag_list))
        print("Mô tả thường:", video_description.strip().lower())
        print("Mô tả hoa:", video_description.strip().upper())

    # Chức năng 2
    elif menu_choice == 2:
        account_name = input("Nhập tên tài khoản: ")

        if account_name.strip() == "":
            print("Tên tài khoản không được rỗng")
        else:
            print("Tên ban đầu:", account_name)
            print("Tên chuẩn hóa:", "@" + account_name.strip().lower())

    # Chức năng 3
    elif menu_choice == 3:
        hashtag = input("Nhập hashtag: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")

        elif not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")

        elif len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")

        elif " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")

        elif not hashtag[1:].replace("_", "").isalnum():
            print("Hashtag chỉ được chứa chữ cái, số hoặc dấu gạch dưới")

        else:
            print("Hashtag hợp lệ")
            hashtag_list.append(hashtag)

    # Chức năng 4
    elif menu_choice == 4:
        if video_description.strip() == "":
            print("Chưa có mô tả video để xử lý")
            continue

        keyword_find = input("Nhập từ khóa cần tìm: ")
        keyword_replace = input("Nhập từ khóa thay thế: ")

        count_keyword = video_description.count(keyword_find)

        if count_keyword > 0:
            new_description = video_description.replace(keyword_find, keyword_replace)

            print("Số lần xuất hiện:", count_keyword)
            print("Mô tả sau thay thế:")
            print(new_description)

            video_description = new_description
        else:
            print("Không tìm thấy từ khóa trong mô tả")

    # Chức năng 5
    elif menu_choice == 5:
        print("Thoát chương trình")
        break
