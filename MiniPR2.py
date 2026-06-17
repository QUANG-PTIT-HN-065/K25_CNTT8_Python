# Hàm hiển thị danh sách đơn hàng
def show_orders(orders_list):
    if not orders_list:
        print("Hệ thống hiện chưa có đơn hàng nào!")
        return
    
    print("--- DANH SÁCH ĐƠN HÀNG ĐẠI LÝ ---")
    print(f"{'MÃ ĐƠN':<10} | {'TÊN ĐẠI LÝ':<25} | {'GIÁ TRỊ (VND)':<15} | {'TRẠNG THÁI':<10}")
    print("-" * 70)
    for order in orders_list:
        print(f"{order['id']:<10} | {order['name']:<25} | {order['price']:<15} | {order['status']:<10}")

# Hàm thêm mới đơn hàng
def create_order(orders_list):
    print("--- TẠO MỚI ĐƠN HÀNG ---")
    order_id = input("Nhập mã đơn hàng: ").strip()
    
    # Kiểm tra trùng mã 
    for order in orders_list:
        if order['id'] == order_id:
            print("[Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống! (ERR-01)")
            return
            
    name = input("Nhập tên đại lý: ").strip()
    while not name:
        name = input("Không được để trống. Nhập tên đại lý: ").strip()
    while True:
        price_str = input("Nhập giá trị đơn hàng (VND): ").strip()
        if price_str.isdigit() and int(price_str) > 0:
            price = int(price_str)
            break
        else:
            print("[Lỗi]: Giá trị đơn hàng phải là số tiền lớn hơn 0! (ERR-02)")
    orders_list.append({'id': order_id, 'name': name, 'price': price, 'status': 'Unpaid'})
    print(f"[Thành công]: Đơn hàng {order_id} đã được tạo thành công!")

# Hàm cập nhật trạng thái
def update_payment_status(orders_list):
    print("--- CẬP NHẬT TRẠNG THÁI THANH TOÁN ---")
    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
    
    # Tìm đơn hàng và xử lý cập nhật
    for order in orders_list:
        if order['id'] == order_id:
            print(f"Tìm thấy đơn hàng của: {order['name']} (Giá trị: {order['price']})")
            if order['status'] == 'Paid':
                print("[Lỗi]: Đơn hàng này đã được thanh toán trước đó! (ERR-04)")
            else:
                order['status'] = 'Paid'
                print(f"[Thành công]: Đơn hàng {order_id} đã được cập nhật trạng thái ĐÃ THANH TOÁN!")
            return
            
    # Báo lỗi nếu không tìm thấy
    print(f"[Lỗi]: Không tìm thấy đơn hàng nào có mã [{order_id}]! (ERR-03)")

# Hàm tính toán doanh thu & chiết khấu
def calculate_financials(orders_list):
    # Lọc và cộng doanh thu các đơn đã thanh toán
    total_revenue = sum(order['price'] for order in orders_list if order['status'] == 'Paid')
    
    # Tính toán chiết khấu
    discount_rate = 5 if total_revenue >= 100000000 else 0
    discount_amount = int(total_revenue * (discount_rate / 100))
    
    return (total_revenue, discount_rate, discount_amount)


# Khởi tạo dữ liệu mẫu
orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]


while True:
    print("\n=========================================")
    print(" QUẢN LÝ ĐƠN HÀNG - AGENT ORDER")
    print("=========================================")
    print("1. Xem danh sách đơn hàng hiện có")
    print("2. Tạo mới đơn hàng đại lý")
    print("3. Cập nhật trạng thái thanh toán")
    print("4. Tính tổng doanh thu & Chiết khấu")
    print("5. Thoát chương trình")
    print("=========================================")
    choice_str = input("Mời chọn chức năng (1-5): ").strip()
    
    if choice_str.isdigit():
        choice = int(choice_str)
        if choice == 1:
            show_orders(orders)
        elif choice == 2:
            create_order(orders)
        elif choice == 3:
            update_payment_status(orders)
        elif choice == 4:
            revenue, rate, amount = calculate_financials(orders)
            print("--- BÁO CÁO TÀI CHÍNH DOANH NGHIỆP ---")
            print(f"+ Tổng doanh thu thực tế (Đã thanh toán): {revenue:,} VND")
            print(f"+ Tỷ lệ chiết khấu áp dụng: {rate}%")
            print(f"+ Số tiền chiết khấu đại lý nhận lại: {amount:,} VND")
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng phần mềm!\n[Chương trình kết thúc]")
            break
        else:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5! (ERR-05)")
    else:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5! (ERR-05)")