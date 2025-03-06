def solution(a, b):
    answer = 0
    a, b = min(a, b), max(a, b)

    while b != a:
        answer += b
        b -= 1
    answer += a

    return answer