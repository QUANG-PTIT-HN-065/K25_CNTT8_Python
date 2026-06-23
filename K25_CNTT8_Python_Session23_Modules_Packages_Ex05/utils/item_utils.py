import random
from utils.player_utils import find_player

rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]

shop_items = {"Potion": 50, "Iron Sword": 200, "Magic Book": 300, "Mana Stone": 150}


def open_treasure_chest(records):
    player_id = input("Nhập mã người chơi: ")
    index = find_player(records, player_id)

    if index == -1:
        print("Không tìm thấy người chơi!")
        return

    reward = random.choice(rewards)

    if reward == "100 Gold":
        records[index]["gold"] += 100
    else:
        records[index]["inventory"].append(reward)

    print("Phần thưởng:", reward)


def buy_item(records):
    player_id = input("Nhập mã người chơi: ")
    index = find_player(records, player_id)

    if index == -1:
        print("Không tìm thấy người chơi!")
        return

    item = input("Nhập vật phẩm: ")

    if item not in shop_items:
        print("Vật phẩm không tồn tại trong cửa hàng!")
        return

    price = shop_items[item]

    if records[index]["gold"] < price:
        print("Không đủ vàng để mua vật phẩm này!")
    else:
        records[index]["gold"] -= price
        records[index]["inventory"].append(item)
        print("Mua thành công!")
