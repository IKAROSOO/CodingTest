def solution(N, stages):
    '''오렐리 게임의 스테이지별 실패율을 계산하고,
    실패율이 높은 순서대로 스테이지 번호를 정렬'''

    '''
    N : 스테이지 수
    stages : 각 플레이어의 도전중인 스테이지 번호
    '''

    answer = []
    players = len(stages)
    reached_stages = []
    cleared_stages = [0]*N
    failed_rate = []
    player_dict = {}
    stages.sort()
    cnt = 0

    for i in range(0, N+2):
        player_dict[i] = 0

    for stage in stages:
        player_dict[stage] += 1
    
    for i in range(N):
        cnt += player_dict[i+1]
        cleared_stages[i] = players - cnt
    
    cnt1 = players

    for i in range(0, N):
        reached_stages.append(cnt1 - cleared_stages[i])
        cnt1 = cleared_stages[i]

    for i in range(N):
        domin = reached_stages[i] + cleared_stages[i]

        if domin != 0:
            failed_rate.append((reached_stages[i] / domin, i+1))
        else:
            failed_rate.append((0, i+1))
    
    sorted_failed_rate = sorted(failed_rate, key=lambda x: (-x[0], x[1]))

    answer = [stage for _, stage in sorted_failed_rate]

    return answer