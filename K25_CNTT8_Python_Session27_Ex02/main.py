"""
1) Phân tích và thiết kế giải pháp

1. Sơ đồ cấu trúc

            BaseProduct (Abstract)
             /                  \
ColdStorageProduct      HazardousProduct
             \                  /
          HybridPremiumProduct

- BaseProduct: Lớp cha, quản lý thông tin và chức năng chung.
- HybridPremiumProduct: Đa kế thừa từ ColdStorageProduct và HazardousProduct, kết hợp quản lý nhiệt độ và giới hạn an toàn.

2. Báo cáo kỹ thuật

- MRO: Python tìm phương thức theo thứ tự:
  HybridPremiumProduct -> ColdStorageProduct -> HazardousProduct -> BaseProduct -> object.
  Nếu có phương thức trùng tên, Python sử dụng phương thức đầu tiên tìm thấy.

- Duck Typing: Hàm vận chuyển chỉ cần đối tượng có phương thức ship_package(), nên có thể thêm nhiều đơn vị vận chuyển mới mà không cần sửa lớp BaseProduct hoặc các lớp sản phẩm.

"""

"""
Amazon Inventory Simulator Pro
================================
Module quản lý hàng hóa kho logistics sử dụng OOP nâng cao:
- Abstract Base Class
- Inheritance & Multiple Inheritance (MRO)
- Operator Overloading
- Duck Typing
- Static Method & Class Method
"""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Lớp trừu tượng định nghĩa bộ khung chuẩn cho mọi loại hàng hóa.
    Không thể khởi tạo trực tiếp - phải kế thừa và implement các abstract methods.
    """

    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000 

    def __init__(self, product_code: str, product_name: str):
        self.product_code = product_code
        self.product_name = product_name
        self.__stock_quantity = 0

    @property
    def stock_quantity(self) -> int | float:
        """Đọc số lượng tồn kho hiện tại (read-only từ bên ngoài)."""
        return self.__stock_quantity

    def _set_stock_quantity(self, value):
        """Phương thức nội bộ để cập nhật tồn kho - chỉ dùng trong class hierarchy."""
        self.__stock_quantity = value


    @property
    def product_name(self) -> str:
        return self.__product_name

    @product_name.setter
    def product_name(self, name: str):
        """Chuẩn hóa tên: strip khoảng trắng thừa và in hoa."""
        self.__product_name = name.strip().upper()

    @abstractmethod
    def import_stock(self, quantity):
        """Nhập hàng vào kho - hành vi tùy từng loại sản phẩm."""
        pass

    @abstractmethod
    def export_stock(self, quantity):
        """Xuất hàng ra khỏi kho - hành vi tùy từng loại sản phẩm."""
        pass

    def __add__(self, other):
        """
        Nạp chồng toán tử +: cộng tổng số lượng tồn kho hai sản phẩm.
        Trả về NotImplemented nếu other không phải BaseProduct.
        """
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity + other.stock_quantity

    def __lt__(self, other):
        """
        Nạp chồng toán tử <: so sánh tồn kho sản phẩm này với sản phẩm kia.
        Trả về NotImplemented nếu other không phải BaseProduct.
        """
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity < other.stock_quantity

    @staticmethod
    def validate_product_code(product_code: str) -> bool:
        """
        @staticmethod: Không cần instance hay class, kiểm tra logic thuần túy.
        Mã sản phẩm hợp lệ: bắt đầu bằng chữ cái, đúng 10 ký tự.
        """
        return len(product_code) == 10 and product_code[0].isalpha()

    @classmethod
    def update_warehouse_name(cls, new_name: str):
        """
        @classmethod: Nhận cls thay vì self, cập nhật class attribute
        trên toàn hệ thống - ảnh hưởng đến mọi instance.
        """
        cls.warehouse_name = new_name
        print(f"Tên chuỗi kho đã được cập nhật thành: {new_name}")

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] {self.product_name} "
            f"(Mã: {self.product_code}) - Tồn kho: {self.stock_quantity}"
        )

class ColdStorageProduct(BaseProduct):
    """
    Hàng đông lạnh - yêu cầu kiểm soát nhiệt độ nghiêm ngặt.
    Khi xuất kho chịu thêm 5% phí hao hụt bảo quản.
    """

    def __init__(
        self, product_code: str, product_name: str, required_temperature: float
    ):
        super().__init__(product_code, product_name)
        self.required_temperature = required_temperature 

    def import_stock(self, quantity):
        """Nhập kho bình thường - không có ràng buộc đặc biệt."""
        if quantity <= 0:
            print("Số lượng nhập phải lớn hơn 0.")
            return False
        self._set_stock_quantity(self.stock_quantity + quantity)
        print(f"Nhập kho thành công! Tồn kho hiện tại: {self.stock_quantity} đơn vị.")
        return True

    def export_stock(self, quantity):
        """
        Xuất kho đặc thù: luôn chịu thêm 5% hao hụt bảo quản
        tính trên số lượng yêu cầu xuất.
        """
        if quantity <= 0:
            print("Số lượng xuất phải lớn hơn 0.")
            return False
        shrinkage = quantity * 0.05  
        total_deducted = quantity + shrinkage
        if total_deducted > self.stock_quantity:
            print(
                f"Giao dịch thất bại! Tồn kho không đủ (cần {total_deducted}, có {self.stock_quantity})."
            )
            return False
        self._set_stock_quantity(self.stock_quantity - total_deducted)
        print(f"Xuất kho thành công!")
        print(f"  Số lượng yêu cầu:                {quantity} đơn vị")
        print(f"  Số lượng hao hụt bảo quản (5%):  {shrinkage} đơn vị")
        print(f"  Tổng số lượng khấu trừ trong kho: {total_deducted} đơn vị")
        print(f"  Tồn kho còn lại:                  {self.stock_quantity} đơn vị")
        return True

    def apply_cooling_cost(self):
        """
        Tính chi phí vận hành máy lạnh phát sinh dựa trên tồn kho và nhiệt độ.
        Công thức: abs(nhiệt độ) * tồn kho * 30 VND
        """
        cost = abs(self.required_temperature) * self.stock_quantity * 30
        print(f"  Số lượng tồn kho hiện tại: {self.stock_quantity} đơn vị")
        print(f"  Nhiệt độ yêu cầu:          {self.required_temperature} độ C")
        print(f"  Chi phí làm lạnh phát sinh: +{cost:,.0f} VND")
        return cost


class HazardousProduct(BaseProduct):
    """
    Hàng hóa nguy hiểm - giới hạn tồn kho tối đa theo hạn mức an toàn.
    Tuyệt đối không được vượt quá max_safety_limit.
    """

    def __init__(self, product_code: str, product_name: str, max_safety_limit: int):
        super().__init__(product_code, product_name)
        self.max_safety_limit = max_safety_limit  

    def import_stock(self, quantity):

        if quantity <= 0:
            print("Số lượng nhập phải lớn hơn 0.")
            return False
        if self.stock_quantity + quantity > self.max_safety_limit:
            print(
                f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá "
                f"hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit})."
            )
            return False
        self._set_stock_quantity(self.stock_quantity + quantity)
        print(f"Nhập kho thành công! Tồn kho hiện tại: {self.stock_quantity} đơn vị.")
        return True

    def export_stock(self, quantity):
        """Xuất kho bình thường theo quy trình an toàn."""
        if quantity <= 0:
            print("Số lượng xuất phải lớn hơn 0.")
            return False
        if quantity > self.stock_quantity:
            print(f"Giao dịch thất bại! Tồn kho không đủ (có {self.stock_quantity}).")
            return False
        self._set_stock_quantity(self.stock_quantity - quantity)
        print(f"Xuất kho thành công! Tồn kho còn lại: {self.stock_quantity} đơn vị.")
        return True


class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):


    def __init__(
        self,
        product_code: str,
        product_name: str,
        required_temperature: float,
        max_safety_limit: int,
    ):
        BaseProduct.__init__(self, product_code, product_name)
        self.required_temperature = required_temperature
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        """
        Tích hợp: kiểm tra hạn mức an toàn (HazardousProduct),
        nếu hợp lệ thì nhập kho bình thường.
        """
        if quantity <= 0:
            print("Số lượng nhập phải lớn hơn 0.")
            return False
        if self.stock_quantity + quantity > self.max_safety_limit:
            print(
                f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá "
                f"hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit})."
            )
            return False
        self._set_stock_quantity(self.stock_quantity + quantity)
        print(f"Nhập kho thành công! Tồn kho hiện tại: {self.stock_quantity} đơn vị.")
        return True

    def export_stock(self, quantity):
        """
        Tích hợp: xuất kho theo logic đông lạnh (hao hụt 5%),
        đồng thời kiểm tra tồn kho không âm.
        """
        return ColdStorageProduct.export_stock(self, quantity)



class FedExCarrier:
    """Đối tác vận chuyển FedEx - Duck Typing: chỉ cần có ship_package()."""

    def ship_package(self, product: BaseProduct, quantity: int):
        print(f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        print(f"Xác thực đối tác bằng Duck Typing thành công!")
        result = product.export_stock(quantity)
        if result:
            print(
                f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity} đơn vị."
            )
            print(f"Số lượng tồn kho cập nhật: {product.stock_quantity} đơn vị.")
        return result


class DHLCarrier:
    """Đối tác vận chuyển DHL - Duck Typing: chỉ cần có ship_package()."""

    def ship_package(self, product: BaseProduct, quantity: int):
        print(f"[Hệ thống DHL]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        print(f"Xác thực đối tác bằng Duck Typing thành công!")
        result = product.export_stock(quantity)
        if result:
            print(
                f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity} đơn vị."
            )
            print(f"Số lượng tồn kho cập nhật: {product.stock_quantity} đơn vị.")
        return result


def dispatch_to_carrier(carrier_agent, product: BaseProduct, quantity: int):
    """
    Hàm toàn cục điều phối vận chuyển - Duck Typing.
    Không quan tâm carrier_agent là lớp gì, miễn là có phương thức ship_package().
    Bẫy 4: Bắt AttributeError nếu carrier không có ship_package().
    """
    try:
        carrier_agent.ship_package(product, quantity)
    except AttributeError:
        print("Lỗi: Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật.")


def print_separator():
    print("-" * 45)


def get_int_input(prompt: str) -> int:
    """Đọc số nguyên dương từ người dùng, xử lý lỗi nhập liệu."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Vui lòng nhập số nguyên dương.")
                continue
            return value
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")


def get_float_input(prompt: str) -> float:
    """Đọc số thực từ người dùng."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập số.")


def menu_register_product(products: list) -> object:
    """Chức năng 1: Đăng ký mã hàng hóa mới."""
    print("\n--- CHỌN LOẠI SẢN PHẨM KHỞI TẠO ---")
    print("1. Cold Storage Product (Hàng Đông Lạnh)")
    print("2. Hazardous Product (Hàng Nguy Hiểm)")
    print("3. Hybrid Premium Product (Hàng Lai Cao Cấp)")

    choice = input("Chọn loại sản phẩm (1-3): ").strip()
    if choice not in ("1", "2", "3"):
        print("Lựa chọn không hợp lệ.")
        return None

    product_code = input("Nhập mã sản phẩm 10 ký tự: ").strip()
    if not BaseProduct.validate_product_code(product_code):
        print(
            "Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng chữ cái."
        )
        return None

    product_name = input("Nhập tên sản phẩm: ")

    product = None

    if choice == "1":
        temp = get_float_input("Nhập nhiệt độ bảo quản yêu cầu (độ C): ")
        product = ColdStorageProduct(product_code, product_name, temp)
        print(f"\nĐăng ký sản phẩm Đông Lạnh thành công!")
        print(f"Tên sản phẩm: {product.product_name}")

    elif choice == "2":
        limit = get_int_input("Nhập hạn mức lưu trữ an toàn tối đa: ")
        product = HazardousProduct(product_code, product_name, limit)
        print(f"\nĐăng ký sản phẩm Nguy Hiểm thành công!")
        print(f"Tên sản phẩm: {product.product_name}")

    elif choice == "3":
        temp = get_float_input("Nhập nhiệt độ bảo quản yêu cầu (độ C): ")
        limit = get_int_input("Nhập hạn mức lưu trữ an toàn tối đa: ")
        product = HybridPremiumProduct(product_code, product_name, temp, limit)
        print(f"\nĐăng ký sản phẩm Hybrid thành công!")
        print(f"Tên sản phẩm: {product.product_name}")

    if product:
        products.append(product)

    return product


def menu_view_info(current_product):
    """Chức năng 2: Xem thông tin & MRO."""
    if current_product is None:
        print("Chưa có sản phẩm nào được chọn. Vui lòng đăng ký sản phẩm trước.")
        return

    print("\n--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
    print(f"Loại sản phẩm:        {current_product.__class__.__name__}")
    print(f"Chuỗi kho:            {current_product.warehouse_name}")
    print(f"Mã sản phẩm:          {current_product.product_code}")
    print(f"Tên sản phẩm:         {current_product.product_name}")
    print(f"Số lượng tồn kho:     {current_product.stock_quantity} đơn vị")

    if hasattr(current_product, "required_temperature"):
        print(f"Nhiệt độ yêu cầu:     {current_product.required_temperature} độ C")
    if hasattr(current_product, "max_safety_limit"):
        print(f"Hạn mức an toàn tối đa: {current_product.max_safety_limit} đơn vị")

    print("\n--- THỨ TỰ KẾ THỪA MRO ---")
    for i, cls in enumerate(type(current_product).__mro__):
        print(f"  {i + 1}. {cls.__name__}")


def menu_transaction(current_product):
    """Chức năng 3: Nhập / Xuất kho (Đa hình)."""
    if current_product is None:
        print("Chưa có sản phẩm nào được chọn.")
        return

    print("\n--- GIAO DỊCH NHẬP / XUẤT KHO ---")
    print("1. Nhập kho")
    print("2. Xuất kho")
    tx = input("Chọn giao dịch (1-2): ").strip()

    if tx == "1":
        qty = get_int_input("Nhập số lượng cần nhập: ")
        current_product.import_stock(qty)
    elif tx == "2":
        qty = get_int_input("Nhập số lượng cần xuất: ")
        current_product.export_stock(qty)
    else:
        print("Lựa chọn không hợp lệ.")


def menu_cooling_cost(current_product):
    """Chức năng 4: Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội."""
    if current_product is None:
        print("Chưa có sản phẩm nào được chọn.")
        return

    print("\n--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")

    if isinstance(current_product, ColdStorageProduct):
        current_product.apply_cooling_cost()
    else:
        print("Sản phẩm này không có tính năng bảo quản đông lạnh. Không hỗ trợ.")


def menu_overloading(current_product, products: list):
    """Chức năng 5: Gộp lô hàng & So sánh tồn kho (Operator Overloading)."""
    if current_product is None:
        print("Chưa có sản phẩm nào được chọn.")
        return

    other_products = [p for p in products if p is not current_product]
    if not other_products:
        print("Không có sản phẩm nào khác trong hệ thống để so sánh.")
        return

    print("\n--- ĐỒNG BỘ & SO SÁNH TỒN KHO (OPERATOR OVERLOADING) ---")
    print(
        f"Sản phẩm hiện tại (A): {current_product.product_name} "
        f"(Tồn kho: {current_product.stock_quantity} đơn vị)"
    )
    print("Danh sách sản phẩm đối ứng (B):")
    for i, p in enumerate(other_products, 1):
        print(
            f"  {i}. {p.product_code} ({p.product_name} - Tồn kho: {p.stock_quantity} đơn vị)"
        )

    try:
        idx = int(input("Chọn sản phẩm đối ứng (B): ")) - 1
        if idx < 0 or idx >= len(other_products):
            print("Lựa chọn không hợp lệ.")
            return
        other = other_products[idx]
    except ValueError:
        print("Dữ liệu không hợp lệ.")
        return

    lt_result = current_product.__lt__(other)
    add_result = current_product.__add__(other)

    if lt_result is NotImplemented:
        print("Lỗi: Không thể so sánh với đối tượng không phải BaseProduct.")
    elif lt_result:
        print(
            f"[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A ÍT HƠN tồn kho sản phẩm B."
        )
    else:
        print(
            f"[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A KHÔNG ÍT HƠN tồn kho sản phẩm B."
        )

    if add_result is NotImplemented:
        print("Lỗi: Không thể cộng với đối tượng không phải BaseProduct.")
    else:
        print(
            f"[Kết quả Tổng hợp (__add__)]: Tổng số lượng tồn kho của cả 2 mã sản phẩm là: "
            f"{add_result} đơn vị."
        )


def menu_duck_typing(current_product):
    """Chức năng 6: Điều phối vận chuyển qua Đối tác thứ ba (Duck Typing)."""
    if current_product is None:
        print("Chưa có sản phẩm nào được chọn.")
        return

    print("\n--- ĐIỀU PHỐI ĐƠN VỊ VẬN CHUYỂN NGOÀI ---")
    print("1. Vận chuyển qua đối tác FedEx")
    print("2. Vận chuyển qua đối tác DHL")
    choice = input("Chọn đối tác vận chuyển (1-2): ").strip()

    qty = get_int_input("Nhập số lượng hàng hóa bàn giao: ")

    if choice == "1":
        carrier = FedExCarrier()
    elif choice == "2":
        carrier = DHLCarrier()
    else:
        print("Lựa chọn không hợp lệ.")
        return

    dispatch_to_carrier(carrier, current_product, qty)


def select_current_product(products: list):
    """Cho phép người dùng chọn sản phẩm đang hoạt động từ danh sách."""
    if not products:
        print("Chưa có sản phẩm nào trong hệ thống.")
        return None

    print("\n--- CHỌN SẢN PHẨM ĐANG HOẠT ĐỘNG ---")
    for i, p in enumerate(products, 1):
        print(f"  {i}. {p.product_code} - {p.product_name} [{p.__class__.__name__}]")
    try:
        idx = int(input("Chọn sản phẩm (số thứ tự): ")) - 1
        if 0 <= idx < len(products):
            return products[idx]
        print("Lựa chọn không hợp lệ.")
    except ValueError:
        print("Dữ liệu không hợp lệ.")
    return None



def main():
    products = []  
    current_product = None  

    while True:
        print("\n" + "=" * 45)
        print("  AMAZON INVENTORY SIMULATOR PRO")
        print("=" * 45)
        if current_product:
            print(
                f"  [Sản phẩm hiện tại]: {current_product.product_name} "
                f"({current_product.__class__.__name__})"
            )
        else:
            print("  [Sản phẩm hiện tại]: Chưa chọn")
        print("-" * 45)
        print("1. Đăng ký mã hàng hóa mới (Chọn loại sản phẩm)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nhập / Xuất kho (Đa hình)")
        print("4. Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội")
        print("5. Kiểm tra tính năng gộp lô hàng & So sánh tồn kho (Overloading)")
        print("6. Điều phối vận chuyển qua Đối tác thứ ba (Duck Typing)")
        print("7. Đổi sản phẩm đang chọn")
        print("8. Thoát chương trình")
        print("=" * 45)

        choice = input("Chọn chức năng (1-8): ").strip()

        if choice == "1":
            new_product = menu_register_product(products)
            if new_product:
                current_product = new_product

        elif choice == "2":
            menu_view_info(current_product)

        elif choice == "3":
            menu_transaction(current_product)

        elif choice == "4":
            menu_cooling_cost(current_product)

        elif choice == "5":
            menu_overloading(current_product, products)

        elif choice == "6":
            menu_duck_typing(current_product)

        elif choice == "7":
            selected = select_current_product(products)
            if selected:
                current_product = selected
                print(f"Đã chuyển sang sản phẩm: {current_product.product_name}")

        elif choice == "8":
            print("\nCảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!")
            break

        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 8.")


def run_edge_case_demo():
    """Demo các bẫy dữ liệu (Edge Cases) - chạy độc lập để kiểm tra."""
    print("\n" + "=" * 50)
    print("EDGE CASE DEMO")
    print("=" * 50)

    print("\n[Bẫy 1] Khởi tạo BaseProduct trực tiếp:")
    try:
        bp = BaseProduct("AMZ1234567", "Test")
    except TypeError as e:
        print(f"  TypeError bắt được: {e}")

    print("\n[Bẫy 2] Vượt quá hạn mức an toàn HazardousProduct:")
    hp = HazardousProduct("AMZ0000001", "Chemical A", 100)
    hp.import_stock(80)
    hp.import_stock(50) 

    print("\n[Bẫy 3] Operator Overloading với String:")
    cp = ColdStorageProduct("AMZ0000002", "Salmon", -18)
    result = cp.__add__("not_a_product")
    print(f"  __add__ với string trả về: {result}")

    print("\n[Bẫy 4] Duck Typing với carrier không hợp lệ:")

    class FakeCarrier:
        def deliver(self):
            pass

    dispatch_to_carrier(FakeCarrier(), cp, 10)


main()
