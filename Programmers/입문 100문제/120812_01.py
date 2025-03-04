def solution(array):
    answer = 0

    memo = {}
    n = len(array)

    for i in range(n):
        if array[i] not in memo:
            memo[array[i]] = 0
        memo[array[i]] += 1

    max_cnt = max(memo.values())
    
    modes = []

    for key, value in memo.items():
        if value == max_cnt:
            modes.append(key)
    
    if len(modes) > 1:
        return -1
    else:
        return modes[0]