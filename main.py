from Manager import *

Manager = ProductManager()


def main():
    while True:
        print(
            "\n================ MENU ================\n"
            "1. Thêm sản phẩm mới\n"
            "2. Hiển thị danh sách sản phẩm \n"
            "3. Cập nhật sản phẩm\n"
            "4. Xóa sản phẩm\n"
            "5. Tìm kiếm sản phẩm\n"
            "6. Thoát\n"
            "====================================="
        )

        while True:
            choice = input("Nhập lựa chọn: ")
            if choice == "1":
                Manager.add_product()
                break
            elif choice == "2":
                Manager.show_all()
                break
            elif choice == "3":
                Manager.update_product()
                break
            elif choice == "4":
                Manager.delete_product()
            elif choice == "5":
                Manager.search_product()
            elif choice == "6":
                print("Thoát chương trình: ")
                return
            else:
                print("Lựa chọn ko hợp lệ: ")
                continue

main()