def solution(answer):
    if len(answer) == m:
        print(*answer)
        return

    for num in range(1, n+1):
        answer.append(num)

        solution(answer)

        answer.pop()

n, m = map(int, input().split())
nums = list(i for i in range(1, n+1))

answer = list()

solution(answer)