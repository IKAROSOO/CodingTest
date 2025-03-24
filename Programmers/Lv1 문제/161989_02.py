def solution(n, m, section):
    cnt = 0
    printed = 0

    for s in section:
        if s > printed:
            cnt += 1
            printed = s + m - 1
    
    return cnt