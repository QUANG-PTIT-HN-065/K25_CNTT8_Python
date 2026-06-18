import logging

logging.basicConfig(
    filename="fantasy_league.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

players = [
    {
        "player_id": "T101",
        "name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0,
    },
    {
        "player_id": "GEN01",
        "name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2,
    },
]


def find_player_by_id(players: list, player_id: str) -> int:
    """Tìm vị trí tuyển thủ."""
    player_id = player_id.strip().upper()

    for i, player in enumerate(players):
        if player.get("player_id", "") == player_id:
            return i

    return -1


def calc_actual_withdrawal(withdraw_amount: int) -> float:
    """Tính token thực nhận."""
    if withdraw_amount < 0:
        raise ValueError

    return withdraw_amount * 0.9


def display_market(players: list) -> None:
    logging.info("User viewed the player market.")

    if not players:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    for player in players:
        token = player.get("fan_tokens", 0)

        if token == 0:
            status = "Chưa có người đầu tư"
        elif token <= 1000:
            status = "Đang thu hút"
        else:
            status = "Tuyển thủ Hot"

        print(
            player.get("player_id", "Unknown"),
            player.get("name", "Unknown"),
            token,
            status,
        )


def invest_tokens(players: list) -> None:
    try:
        player_id = input("Nhập mã: ").strip().upper()
        index = find_player_by_id(players, player_id)

        if index == -1:
            logging.warning(f"Invest failed - Player {player_id} not found")
            return

        amount = int(input("Nhập token: "))

        if amount <= 0:
            raise ValueError

        players[index]["fan_tokens"] += amount

        logging.info(f"Invested {amount} tokens into {player_id}")

    except ValueError:
        logging.warning("Invalid token input while investing")


def withdraw_tokens(players: list) -> None:
    try:
        player_id = input("Nhập mã: ").strip().upper()
        index = find_player_by_id(players, player_id)

        if index == -1:
            return

        amount = int(input("Nhập token rút: "))

        if amount > players[index]["fan_tokens"]:
            logging.warning("Withdraw failed - Amount exceeds current fan tokens")
            return

        players[index]["fan_tokens"] -= amount

        actual = calc_actual_withdrawal(amount)

        logging.info(
            f"Withdrawn {amount} tokens from {player_id}. Actual received: {actual}"
        )

    except ValueError:
        pass


def update_form(players: list) -> None:
    try:
        player_id = input("Nhập mã: ").strip().upper()
        index = find_player_by_id(players, player_id)

        if index == -1:
            return

        multiplier = float(input("Nhập hệ số: "))

        if multiplier < 0.5 or multiplier > 2.5:
            raise ValueError

        players[index]["form_multiplier"] = multiplier

        logging.info(f"Updated form multiplier for {player_id} to {multiplier}")

    except ValueError:
        pass


def calculate_match_points(players: list) -> None:
    try:
        player_id = input("Nhập mã: ").strip().upper()
        index = find_player_by_id(players, player_id)

        if index == -1:
            return

        base_points = int(input("Nhập điểm gốc: "))

        earned_points = base_points * players[index]["form_multiplier"]

        players[index]["match_points"] += earned_points

        logging.info(f"Added {earned_points} match points to {player_id}")

    except ValueError:
        pass
