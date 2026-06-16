products = [
    {"id": "P01", "name": "Coca Cola", "price": 15000},
    {"id": "P02", "name": "Bánh mì", "price": 20000},
]
number = 3
next_id = f"P{number}"


def add_item():
    id = next_id
    name = input("nhập tên sản phẩm: ")
    price = int(input("Nhập giá tiền: "))

    new_item = {"id": id, "name": name, "price": price}

    products.append(new_item)
    print("thêm thành công")


def show():
    if not products:
        print("Danh sách sản phẩm rỗng!")
        return

    print(f"{'ID':<10}{'Tên sản phẩm':<25}{'Giá':>15}")
    print("-" * 50)

    for product in products:
        print(
            f"{product['id']:<10}|"
            f"{product['name']:<25}|"
            f"{product['price']:>15,}"
        )



def update(id):
    for i in products:
        if i["id"] == id:
            new_price = int(input("Nhập giá tiền mới: "))
            i["price"] = new_price
            return print("Cập nhật thành công!")

    print("Không tìm thấy sản phẩm!")


while True:
    print("quản lý cửa hàng")
    print("1. xem danh sách")
    print("2. Thêm mới 1 sản phẩm")
    print("3. cập nhật giá tiền")
    print("5. thoát")
    
    choice = int(input("nhập lựa chọn: "))
    
    if choice < 1 or choice > 5:
        continue
    if choice == 1:
        number += 1
        show()
    elif choice == 2:
        add_item()
    elif choice == 3:
        id = input("nhập id sản phẩm: ")
        update(id)
    elif choice == 4:
        print("kết thúc chương trình")
        break