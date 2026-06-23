import random as rd
from utils.player_utils import find_player

monsters = [
    {"name": "Bug Python", "damage": 20, "reward_gold": 100},
    {"name": "Import Error", "damage": 35, "reward_gold": 150},
    {"name": "Module Not Found", "damage": 50, "reward_gold": 250},
]


def fight_monster(records):
    player_id = input("Nhập mã người chơi: ")
    index = find_player(records, player_id)

    if index == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[index]

    if player["hp"] <= 0:
        print("Người chơi đã gục ngã, không thể tiếp tục chiến đấu!")
        return

    monster = rd.choice(monsters)

    player["hp"] -= monster["damage"]

    if player["hp"] > 0:
        player["gold"] += monster["reward_gold"]
        print("Chiến thắng!")
    else:
        print("Thất bại!")
