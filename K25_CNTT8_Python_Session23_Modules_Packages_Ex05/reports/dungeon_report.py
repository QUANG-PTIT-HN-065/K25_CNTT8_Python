from operator import itemgetter


def display_players(records):
    for player in records:
        if player["hp"] <= 0:
            status = "Đã gục ngã"
        elif player["hp"] < 50:
            status = "Nguy hiểm"
        elif player["hp"] < 100:
            status = "Ổn định"
        else:
            status = "Sung sức"

        print(player["player_id"], player["name"], status)


def show_leaderboard(records):
    ranking = sorted(
        records, key=lambda x: (x["level"], x["gold"], x["hp"]), reverse=True
    )

    for i, player in enumerate(ranking, 1):
        print(i, player["name"], player["level"])
