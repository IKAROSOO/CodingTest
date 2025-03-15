def solution(number):
    from itertools import combinations
    cnt = 0

    for num in combinations(number, 3):
        if sum(num) == 0:
            cnt += 1

    return cnt