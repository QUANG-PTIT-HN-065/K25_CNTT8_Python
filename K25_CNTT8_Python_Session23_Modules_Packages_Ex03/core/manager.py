from datetime import datetime


def check_duplicate_id(flight_id, flight_list):
    flight_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"] == flight_id:
            return True
    return False


def add_flight(flights):
    flight_id = input("Nhập mã chuyến bay: ").strip().upper()

    if check_duplicate_id(flight_id, flights):
        print("Mã chuyến bay đã tồn tại!")
        return

    passengers = int(input("Nhập số lượng hành khách: "))
    depart_time = input("Nhập thời gian cất cánh: ")

    try:
        datetime.strptime(depart_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Sai định dạng thời gian!")
        return

    duration_min = int(input("Nhập số phút bay: "))

    flights.append(
        {
            "flight_id": flight_id,
            "passengers": passengers,
            "depart_time": depart_time,
            "duration_min": duration_min,
        }
    )

    print("Thêm chuyến bay thành công!")
