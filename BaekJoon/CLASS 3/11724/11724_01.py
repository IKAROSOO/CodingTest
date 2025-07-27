import sys
from collections import deque

input = sys.stdin.readline

def solution(start_node):
    global visited

    visited[start_node] = True

    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        for neighbor in range(1, n+1):
            if graph[node][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n, m = map(int, input().split())

cnt = 0
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())

    graph[u][v] = True
    graph[v][u] = True

for i in range(1, n+1):
    if not visited[i]:
        solution(i)
        cnt += 1

print(cnt)