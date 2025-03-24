def solution(players, callings):
    player_rank = {player:rank for rank, player in enumerate(players)}

    for call in callings:
        current_rank = player_rank[call]
        prev_player = players[current_rank-1]

        players[current_rank-1], players[current_rank] = call, prev_player
        player_rank[call], player_rank[prev_player] = current_rank-1, current_rank
    
    return players