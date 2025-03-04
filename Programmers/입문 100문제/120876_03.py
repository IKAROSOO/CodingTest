def solution(lines):
    events = []
    for a, b in lines:
        events.append((min(a, b), 1))  # 시작점
        events.append((max(a, b), -1)) # 끝점
        
    events.sort() # 이벤트 정렬

    overlap = 0
    total_length = 0
    for i in range(len(events) - 1):
        overlap += events[i][1]
        if overlap >= 2: # 두 개 이상의 선분이 겹치는 경우
            total_length += events[i+1][0] - events[i][0]

    return total_length

solution([[0, 5], [3, 9], [1, 10]])


# 제미나이가 추천한 해결법