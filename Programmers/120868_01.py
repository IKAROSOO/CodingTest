def solution(sides):
    cnt = 0

    max_length = sides[0] + sides[1]
    min_length = abs(sides[0] - sides[1])

    for _ in range(min_length, max_length):
        cnt += 1
    
    return cnt-1