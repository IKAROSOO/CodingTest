import sys
from collections import deque

input = sys.stdin.readline

def solution(start_node):
    global graph, visited

    if not visited[start_node]:
        global cnt
        cnt += 1
    
    if visited[start_node]:
        return

    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

cnt = 0

for i in range(1, n+1):
    solution(i)

print(cnt)