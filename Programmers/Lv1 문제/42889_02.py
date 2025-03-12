def solution(N, stages):
    '''오렐리 게임의 스테이지별 실패율을 계산하고,
    실패율이 높은 순서대로 스테이지 번호를 정렬'''

    '''
    N : 스테이지 수
    stages : 각 플레이어의 도전중인 스테이지 번호
    '''

    result = {}
    dominator = len(stages)

    for stage in range(1, N+1):
        if dominator != 0:
            cnt = stages.count(stage)
            result[stage] = cnt / dominator
            dominator -= cnt
        else:
            result[stage] = 0
    
    return sorted(result, key=lambda x: result[x], reverse=True)