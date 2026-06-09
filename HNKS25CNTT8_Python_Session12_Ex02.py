# # 1) Phân tích Input/Output
# # Input

# # Chức năng 2 - Mở sổ
# # account_id: str
# # customer_name: str
# # balance: int > 0
# # term_months: int > 0
# # interest_rate: float > 0
# # Chức năng 3 - Cập nhật
# # account_id: str
# # customer_name: str
# # balance: int > 0
# # term_months: int > 0
# # interest_rate: float > 0
# # Chức năng 4 - Tất toán
# # account_id: str
# # Chức năng 5 - Tính lãi
# # account_id: str
# # Chức năng 6 - Rút trước hạn
# # account_id: str
# # actual_months: int > 0
# # Menu
# # choice: int (1-7)

# # Output
# # Chức năng 1

# # Hiển thị danh sách sổ tiết kiệm.

# # Chức năng 2

# # Thêm sổ mới hoặc thông báo lỗi.

# # Chức năng 3

# # Cập nhật thông tin hoặc thông báo lỗi.

# # Chức năng 4

# # Đổi trạng thái sang "closed".

# # Chức năng 5

# # Hiển thị:

# # Tiền lãi dự kiến
# # Tổng tiền nhận
# # Chức năng 6

# # Hiển thị:

# # Tiền lãi thực nhận
# # Tổng tiền thực nhận
# # Chức năng 7

# # Thoát chương trình.

# # Đề xuất giải pháp
# # Dùng list chứa các dictionary.
# # Chuẩn hóa mã sổ bằng:
# # account_id = account_id.strip().upper()
# # Kiểm tra trùng mã bằng vòng lặp.
# # Kiểm tra trạng thái "active" trước khi cập nhật, tính lãi hoặc rút trước hạn.
# # Tính lãi đến hạn:
# # interest = balance * interest_rate / 100 * term_months / 12
# # Tính lãi rút trước hạn:
# # interest = balance * applied_rate / 100 * actual_months / 12

# # Pseudocode

# Khởi tạo saving_accounts

# Lặp vô hạn
#     Hiển thị menu
#     Nhập lựa chọn
#     Nếu chọn 1
#         Hiển thị danh sách
#     Nếu chọn 2
#         Nhập thông tin
#         Kiểm tra dữ liệu
#         Kiểm tra trùng mã
#         Thêm mới
#     Nếu chọn 3
#         Nhập mã sổ
#         Tìm sổ
#         Kiểm tra active
#         Cập nhật
#     Nếu chọn 4
#         Nhập mã sổ
#         Tìm sổ
#         Đổi trạng thái closed
#     Nếu chọn 5
#         Nhập mã sổ
#         Tìm sổ
#         Kiểm tra active
#         Tính lãi dự kiến
#     Nếu chọn 6
#         Nhập mã sổ
#         Nhập số tháng thực gửi
#         Tìm sổ
#         Kiểm tra active
#         Nếu actual_months < term_months
#             dùng lãi suất 0.5%
#         Ngược lại
#             dùng lãi suất của sổ
#         Tính tiền lãi
#         Tính tổng tiền nhận
#     Nếu chọn 7
#         Thoát
#     Ngược lại
#         Báo lỗi menu

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active",
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active",
    },
]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến")
    print("6. Kiểm tra rút trước hạn")
    print("7. Thoát")

    try:
        choice = int(input("Nhập lựa chọn: "))

        if choice == 1:

            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")

                for i, account in enumerate(saving_accounts, start=1):
                    print(
                        f"{i}. Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )

        elif choice == 2:

            account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            customer_name = input("Nhập tên khách hàng: ").strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            duplicated = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    duplicated = True
                    break

            if duplicated:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            try:
                balance = int(input("Nhập số tiền gửi: "))
                term_months = int(input("Nhập kỳ hạn gửi theo tháng: "))

                if balance <= 0 or term_months <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue

            except ValueError:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            try:
                interest_rate = float(input("Nhập lãi suất năm: "))

                if interest_rate <= 0:
                    print("Lãi suất không hợp lệ!")
                    continue

            except ValueError:
                print("Lãi suất không hợp lệ!")
                continue

            saving_accounts.append(
                {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": balance,
                    "term_months": term_months,
                    "interest_rate": interest_rate,
                    "status": "active",
                }
            )

            print("Mở sổ tiết kiệm thành công!")

        elif choice == 3:

            account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:

                    found = True

                    if account["status"] == "closed":
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break

                    customer_name = input("Nhập tên khách hàng mới: ").strip()

                    if customer_name == "":
                        print("Tên khách hàng không được để trống")
                        break

                    try:
                        balance = int(input("Nhập số tiền gửi mới: "))
                        term_months = int(input("Nhập kỳ hạn mới: "))

                        if balance <= 0 or term_months <= 0:
                            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                            break

                    except ValueError:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break

                    try:
                        interest_rate = float(input("Nhập lãi suất năm mới: "))

                        if interest_rate <= 0:
                            print("Lãi suất không hợp lệ!")
                            break

                    except ValueError:
                        print("Lãi suất không hợp lệ!")
                        break

                    account["customer_name"] = customer_name
                    account["balance"] = balance
                    account["term_months"] = term_months
                    account["interest_rate"] = interest_rate

                    print("Cập nhật thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")

        elif choice == 4:

            account_id = (
                input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            )

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:

                    account["status"] = "closed"
                    found = True

                    print("Tất toán thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        elif choice == 5:

            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:

                    found = True

                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    interest = (
                        account["balance"]
                        * account["interest_rate"]
                        / 100
                        * account["term_months"]
                        / 12
                    )

                    total = account["balance"] + interest

                    print("Tiền lãi dự kiến:", interest)
                    print("Tổng tiền nhận:", total)

                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        elif choice == 6:

            account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

            try:
                actual_months = int(input("Nhập số tháng thực gửi: "))

                if actual_months <= 0:
                    print("Số tháng thực gửi không hợp lệ!")
                    continue

            except ValueError:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:

                    found = True

                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    if actual_months < account["term_months"]:
                        applied_rate = 0.5
                    else:
                        applied_rate = account["interest_rate"]

                    interest = (
                        account["balance"] * applied_rate / 100 * actual_months / 12
                    )

                    total = account["balance"] + interest

                    print("Tiền lãi thực nhận:", interest)
                    print("Tổng tiền thực nhận:", total)

                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        elif choice == 7:
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
