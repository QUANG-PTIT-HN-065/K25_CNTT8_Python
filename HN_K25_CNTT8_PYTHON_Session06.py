laptop = 0
phone = 0
tablet = 0

while True:
    print("\n===== QUẢN LÝ TỒN KHO CỬA HÀNG CÔNG NGHỆ =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == "1":
        print("\n===== BÁO CÁO TỒN KHO =====")
        print(f"Laptop: {laptop}")
        print(f"Phone: {phone}")
        print(f"Tablet: {tablet}")

        print("\n===== BIỂU ĐỒ TỒN KHO =====")

        print(f"Laptop ({laptop}): ", end="")
        for i in range(laptop):
            print("*", end="")
        print()

        print(f"Phone ({phone}): ", end="")
        for i in range(phone):
            print("*", end="")
        print()

        print(f"Tablet ({tablet}): ", end="")
        for i in range(tablet):
            print("*", end="")
        print()

    elif lua_chon == "2":
        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        mat_hang = input("Chọn mặt hàng cần nhập: ")

        while True:
            so_luong = int(input("Nhập số lượng cần thêm: "))

            if so_luong < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
            else:
                break

        if mat_hang == "1":
            laptop += so_luong
            print("Nhập kho Laptop thành công!")

        elif mat_hang == "2":
            phone += so_luong
            print("Nhập kho Phone thành công!")

        elif mat_hang == "3":
            tablet += so_luong
            print("Nhập kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

    elif lua_chon == "3":
        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        mat_hang = input("Chọn mặt hàng cần xuất: ")

        while True:
            so_luong = int(input("Nhập số lượng cần xuất: "))

            if so_luong < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
            else:
                break

        if mat_hang == "1":
            if so_luong > laptop:
                print("Không đủ hàng!")
            else:
                laptop -= so_luong
                print("Xuất kho Laptop thành công!")

        elif mat_hang == "2":
            if so_luong > phone:
                print("Không đủ hàng!")
            else:
                phone -= so_luong
                print("Xuất kho Phone thành công!")

        elif mat_hang == "3":
            if so_luong > tablet:
                print("Không đủ hàng!")
            else:
                tablet -= so_luong
                print("Xuất kho Tablet thành công!")

        else:
            print("Mặt hàng không hợp lệ!")

    elif lua_chon == "4":
        print("\n===== KIỂM TRA TỒN KHO =====")

        if laptop < 10:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")

        if phone < 10:
            print(f"[CẢNH BÁO] Mặt hàng Phone sắp hết (Chỉ còn {phone} sản phẩm)")

        if tablet < 10:
            print(f"[CẢNH BÁO] Mặt hàng Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")

    elif lua_chon == "5":
        print("Đã thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")