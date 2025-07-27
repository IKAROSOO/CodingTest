from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(r, c, graph, m, n):
    global visited

    visited[r][c] = True

    queue = deque([(r, c)])

    while queue:
        node_r, node_c = queue.popleft()

        for i in range(4):
            next_r = node_r+dx[i]
            next_c = node_c+dy[i]

            if 0 <= next_r < m and 0 <= next_c < n:
                if graph[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())

    graph = [[False] * (n+1) for _ in range(m+1)]
    visited = [[False] * (n+1) for _ in range(m+1)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = True

    for r in range(m):
        for c in range(n):
            if graph[r][c] and not visited[r][c]:
                solution(r, c, graph, m ,n)
                cnt += 1
    
    print(cnt)
