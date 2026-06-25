"""
1) Phân tích giải pháp
Thiết kế Class

Sử dụng Name Mangling (__) cho hai thuộc tính:

__password: Ẩn mật khẩu, không cho phép truy cập trực tiếp từ bên ngoài lớp
__plan: Ẩn thông tin gói cước, chỉ được thay đổi thông qua phương thức upgrade_plan()

Việc sử dụng __ giúp tăng tính bảo mật và kiểm soát dữ liệu tốt hơn

Phân biệt Method
Static Method validate_email():
- Dùng để kiểm tra định dạng email, không cần truy cập dữ liệu của đối tượng hay lớp

Class Method update_max_profiles():
- Dùng để thay đổi giới hạn Profile chung của hệ thống.
- Khi giá trị max_profiles được cập nhật, tất cả các tài khoản hiện có và tài khoản tạo mới đều tự động áp dụng giới hạn mới

"""


class NetflixAccount:
    """
    NetflixAccount class demonstrates:
    - Encapsulation with private attributes (__password, __plan)
    - @property and setter
    - @staticmethod
    - @classmethod
    """

    # Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        """
        Hide the real password when accessed.
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Validate password length before updating.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        """
        Read-only property for subscription plan.
        """
        return self.__plan

    @staticmethod
    def validate_email(email):
        """
        Validate email format.
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        Update profile limit for the whole system.
        """
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        """
        Add a profile if account has not reached limit.
        """
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return

        self.profiles.append(profile_name)
        print(f"Đã thêm Profile: {profile_name}")

    def upgrade_plan(self, new_plan):
        """
        Upgrade subscription plan.
        """
        valid_plans = ["Basic", "Standard", "Premium"]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ")
            return

        self.__plan = new_plan
        print(f"Nâng cấp thành công lên gói {new_plan}")

    def display_info(self):
        """
        Display account information.
        """
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Nền tảng: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước: {self.plan}")

        if self.profiles:
            print("Danh sách Profile:")
            for index, profile in enumerate(self.profiles, start=1):
                print(f"{index}. {profile}")
        else:
            print("Danh sách Profile: Chưa có")


def register_account():
    while True:
        email = input("Nhập Email: ").strip()

        if not NetflixAccount.validate_email(email):
            print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
            continue

        account = NetflixAccount(email)

        while True:
            try:
                password = input("Nhập mật khẩu: ").strip()
                account.password = password
                break
            except ValueError as e:
                print(e)

        print("Đăng ký tài khoản thành công!")
        return account


def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix")
        print("6. Thoát chương trình")
        print("===================================")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")
            current_account = register_account()

        elif choice == "2":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                continue

            current_account.display_info()

        elif choice == "3":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                continue

            print("\n--- THÊM PROFILE ---")
            profile_name = input("Nhập tên Profile: ").strip()

            if not profile_name:
                print("Tên Profile không được để trống")
                continue

            current_account.add_profile(profile_name)

        elif choice == "4":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                continue

            print("\n--- NÂNG CẤP GÓI CƯỚC ---")
            print("1. Basic")
            print("2. Standard")
            print("3. Premium")

            option = input("Chọn gói cước: ").strip()

            plans = {"1": "Basic", "2": "Standard", "3": "Premium"}

            if option not in plans:
                print("Lựa chọn không hợp lệ")
                continue

            current_account.upgrade_plan(plans[option])

        elif choice == "5":
            print("\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---")

            try:
                new_limit = int(input("Nhập giới hạn Profile tối đa mới: "))

                if new_limit <= 0:
                    print("Giới hạn phải lớn hơn 0")
                    continue

                NetflixAccount.update_max_profiles(new_limit)

                print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}")

            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ")

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng Netflix Account Manager!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()
