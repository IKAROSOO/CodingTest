from collections import deque

def solution(start_node=1):
    global visited

    visited[start_node] = True
    queue = deque([start_node])

    cnt = 0

    while queue:
        cur_node = queue.popleft()

        for neighbor in range(1, n+1):
            if graph[cur_node][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1
    
    return cnt

n = int(input())
t = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(t):
    r, c = map(int, input().split())

    graph[r][c] = True
    graph[c][r] = True

answer = solution()

print(answer)

'''
2025_07_17_10:55
'''