import logging

# Cấu hình logging hệ thống
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logger = logging.getLogger(__name__)


def get_shipping_rate(method: str, distance: int) -> float:
    """
    Trả về chi phí vận chuyển cơ sở dựa trên
    phương thức và khoảng cách.
    """

    logger.info(
        f"Đang tính phí giao hàng cho phương thức {method} "
        f"với khoảng cách {distance} km"
    )

    # Kiểm tra dữ liệu đầu vào
    if distance <= 0:
        raise ValueError("Distance must be positive")

    # Xác định phí cơ sở
    if method == "standard":
        base_rate = 15000
    elif method == "express":
        base_rate = 30000
    elif method == "next_day":
        base_rate = 50000
    else:
        base_rate = 20000

    # Phụ thu nếu khoảng cách từ 20km trở lên
    if distance >= 20:
        base_rate += 10000

    logger.info(f"Phí cơ sở sau khi tính = {base_rate}")

    return base_rate


def calculate_final_shipping(weight: float, distance: int, method: str) -> float:
    """
    Tính tổng phí vận chuyển cuối cùng.
    """

    if weight < 0:
        raise ValueError("Trọng lượng hàng hóa không được âm")

    logger.info("Bắt đầu tính tổng phí vận chuyển")

    base_rate = get_shipping_rate(method, distance)

    # 2.000đ mỗi kg
    total_cost = base_rate + weight * 2000

    logger.warning(f"Kết quả: Tổng phí vận chuyển = {total_cost}")

    return total_cost


if __name__ == "__main__":

    test_cases = [
        (3.5, 25, "express"),
        (2.0, -5, "standard"),
    ]

    for weight, distance, method in test_cases:
        try:
            cost = calculate_final_shipping(weight, distance, method)

            logger.info(f"Chi phí cuối cùng: {cost}")

        except ValueError as error:
            logger.error(error)
