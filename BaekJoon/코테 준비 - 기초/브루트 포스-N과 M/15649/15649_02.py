def solution(n, m, answer, visited, nums):
    if len(answer) == m:
        print(*answer)
        return

    for num in nums:
        if not visited[num]:
            visited[num] = True
            answer.append(num)
        
            solution(n, m, answer, visited, nums)

            visited[num] = False
            answer.pop()

n, m = map(int, input().split())
nums = list(i for i in range(1, n+1))
answer = list()
visited = [False] * (n+1)

solution(n, m, answer, visited, nums)

'''
기본적으로 itertools라이브러리의 permutations를 사용하면 금방 풀 수 있지만,
백트래킹을 직접 구현해보기 위하여 이렇게 풀었다.

다시 풀어볼 필요가 있다.
'''