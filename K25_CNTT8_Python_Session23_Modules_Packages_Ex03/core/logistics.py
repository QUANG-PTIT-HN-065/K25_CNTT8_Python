import math


def show_flights(flights):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    for i, flight in enumerate(flights, 1):
        water_boxes = math.ceil(flight["passengers"] / 10)
        print(
            f"{i}. Mã: {flight['flight_id']} | Khởi hành: {flight['depart_time']} | Số khách: {flight['passengers']} | Dự phòng: {water_boxes} thùng nước."
        )
