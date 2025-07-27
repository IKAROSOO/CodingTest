from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(node_r, node_c, farm, visited):
    visited[node_r][node_c] = True

    queue = deque([(node_r, node_c)])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            next_r = r + dx[i]
            next_c = c + dy[i]

            if (0 <= next_r < len(farm) and 0 <= next_c < len(farm[0])
                and not visited[next_r][next_c] and farm[next_r][next_c]):
                
                visited[next_r][next_c] = True
                queue.append((next_r, next_c))

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())

    farm = [[False] * m for _ in range(n)]

    for _ in range(k):
        r, c = map(int, input().split())

        farm[c][r] = True
    
    visited = [[False] * (m) for _ in range(n)]

    cnt = 0

    for i in range(n):
        for j in range(m):
            if farm[i][j] and not visited[i][j]:
                solution(i, j, farm, visited)
                cnt += 1
    
    print(cnt)

'''
2025_07_17_15:30
'''