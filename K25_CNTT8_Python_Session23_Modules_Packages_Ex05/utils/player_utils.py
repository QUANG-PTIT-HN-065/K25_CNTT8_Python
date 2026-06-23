def find_player(records, player_id):
    player_id = player_id.strip().upper()

    for i, player in enumerate(records):
        if player["player_id"] == player_id:
            return i

    return -1
