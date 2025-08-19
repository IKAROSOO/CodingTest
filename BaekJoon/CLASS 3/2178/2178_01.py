from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(start_node=(0, 0)):
    global visited

    visited[start_node[0]][start_node[1]] = True
    queue = deque([(start_node[0], start_node[1], 1)])

    while queue:
        r, c, cnt = queue.popleft()

        if r == n-1 and c == m-1:
            return cnt

        for i in range(4):
            next_r, next_c = r+dx[i], c+dy[i]

            if 0 <= next_r < n and 0 <= next_c < m:
                if maze[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c, cnt+1))

n, m = map(int, input().split())
maze = list()

for _ in range(n):
    nums = input()
    maps = list()
    
    for i in range(m):
        maps.append(int(nums[i]))
    
    maze.append(maps)

visited = [[False] * (m) for _ in range(n)]

answer = solution()

print(answer)