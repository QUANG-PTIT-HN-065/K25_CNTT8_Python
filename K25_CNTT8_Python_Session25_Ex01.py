"""
1) Phân tích và thiết kế giải pháp
1. Thiết kế Class BankAccount

Class Attributes
- bank_name = "Vietcombank"
- transaction_fee = 2000

Private Instance Attributes
- __account_number: Số tài khoản
- __account_name: Tên chủ tài khoản
- __balance: Số dư tài khoản (mặc định 0)

Property

Chỉ đọc số dư

@property
def balance(self)
Cho phép xem số dư.
Không có setter để tránh sửa trực tiếp từ bên ngoài.

Quản lý tên chủ tài khoản

@property
def account_name(self)

@account_name.setter
def account_name(self, new_name)
Tự động loại bỏ khoảng trắng thừa.
Chuyển thành chữ in hoa.
Không cho phép tên rỗng hoặc chỉ chứa khoảng trắng.
2. Thiết kế Method
Static Method
@staticmethod
validate_account_number(account_number)

Mục đích:

- Kiểm tra số tài khoản có đúng 10 chữ số hay không
- Không sử dụng dữ liệu của đối tượng (self)
- Không sử dụng dữ liệu của lớp (cls)

Lý do dùng @staticmethod:

- Chỉ thực hiện chức năng kiểm tra dữ liệu độc lập
- Không phụ thuộc vào trạng thái của class hoặc object

Class Method
@classmethod
update_transaction_fee(cls, new_fee)

Mục đích:

- Thay đổi phí giao dịch dùng chung cho toàn bộ tài khoản

Lý do dùng @classmethod:

- Cần truy cập và cập nhật Class Attribute transaction_fee
- Khi thay đổi phí, mọi đối tượng của lớp đều áp dụng mức phí mới

Instance Methods

deposit(amount)
- Nạp tiền vào tài khoản.
- Kiểm tra số tiền phải lớn hơn 0.
- Cộng tiền vào __balance.
withdraw(amount)
- Rút tiền khỏi tài khoản.
- Kiểm tra số tiền phải lớn hơn 0
- Tổng số tiền bị trừ:

amount + transaction_fee

- Chỉ cho phép rút khi số dư đủ thanh toán tiền rút và phí giao dịch.
display_info()
Hiển thị:
- Tên ngân hàng
- Số tài khoản
- Tên chủ tài khoản
- Số dư hiện tại
- Phí giao dịch hiện hành

"""


class BankAccount:

    # Class Attributes

    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = ""
        self.account_name = account_name
        self.__balance = 0

    # Read-only Property

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        new_name = new_name.strip()

        if new_name == "":
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = new_name.upper()

    @property
    def account_number(self):
        return self.__account_number

    # Static Method

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    # Class Method

    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    # Instance Methods

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print(
                "Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        return True

    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


# Main Program

current_account = None

while True:

    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")

    choice = input("Chọn chức năng (1-6): ")

    # Open Account

    if choice == "1":

        print("\n--- MỞ TÀI KHOẢN MỚI ---")

        while True:
            account_number = input("Nhập số tài khoản 10 chữ số: ")

            if BankAccount.validate_account_number(account_number):
                break

            print("Số tài khoản không hợp lệ!")
            print("Số tài khoản phải gồm đúng 10 chữ số.")

        account_name = input("Nhập tên chủ tài khoản: ")

        current_account = BankAccount(account_number, account_name)

        print("Mở tài khoản thành công!")
        print("Số tài khoản:", current_account.account_number)
        print("Tên chủ tài khoản:", current_account.account_name)

    # Display Account

    elif choice == "2":

        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        else:
            current_account.display_info()

    # Transaction

    elif choice == "3":

        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            continue

        print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
        print("1. Nạp tiền")
        print("2. Rút tiền")

        transaction = input("Chọn loại giao dịch (1-2): ")

        try:
            amount = int(input("Nhập số tiền giao dịch: "))
        except:
            print("Số tiền không hợp lệ")
            continue

        if transaction == "1":
            if current_account.deposit(amount):
                print(f"Số dư mới: {current_account.balance:,} VND")

        elif transaction == "2":
            if current_account.withdraw(amount):
                print(f"Số dư mới: {current_account.balance:,} VND")
            else:
                print(f"Số dư mới: {current_account.balance:,} VND")

        else:
            print("Lựa chọn không hợp lệ")

    # Update Name

    elif choice == "4":

        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            continue

        print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")

        old_name = current_account.account_name
        new_name = input("Nhập tên mới: ")

        current_account.account_name = new_name

        if current_account.account_name != old_name:
            print("Cập nhật thành công.")
            print("Tên mới:", current_account.account_name)

    # Update Fee

    elif choice == "5":

        print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
        print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")

        try:
            new_fee = int(input("Nhập phí giao dịch mới: "))
        except:
            print("Phí giao dịch không hợp lệ")
            continue

        if new_fee < 0:
            print("Phí giao dịch không được âm")
            print(f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND")
        else:
            BankAccount.update_transaction_fee(new_fee)
            print(
                f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND"
            )

    # Exit

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
        break

    else:
        print("Lựa chọn không hợp lệ")
