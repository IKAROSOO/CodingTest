def solution(answer):
    global visited

    if len(answer) == m:
        print(*answer)
        return
    
    cnt = 1
    if answer:
        cnt = answer[-1] + 1
    
    for num in range(cnt, n+1):
        if not visited[num]:
            answer.append(num)
            visited[num] = True

            solution(answer)

            visited[num] = False
            answer.pop()

n, m = map(int, input().split())
nums = list(i for i in range(1, n+1))

visited = [False] * (n+1)
answer = list()

solution(answer)