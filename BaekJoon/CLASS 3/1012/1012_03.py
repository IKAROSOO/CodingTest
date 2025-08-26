from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c):
    global visited

    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            next_r, next_c = cur_r + dx[i], cur_c + dy[i]
            if 0 <= next_r < n and 0 <= next_c < m:
                if farm[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    
    print(cnt)

'''
2025_08_26_21:34
'''