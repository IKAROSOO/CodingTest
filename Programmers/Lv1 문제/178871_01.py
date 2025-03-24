def solution(players, callings):
    for change in callings:
        rank = players.index(change)+1
        tmp = players[rank-1]

        players[rank-1] = change
        players[rank] = tmp
    
    print(players)

'''
시간복잡도로 인해 실패
'''