def solution(n):
    answer = 0
    cnt = 0

    while cnt < n:
        answer += 1

        if answer % 3 == 0 or "3" in str(answer):
            continue
        cnt += 1

    return answer