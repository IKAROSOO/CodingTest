from collections import deque

def solution(node):
    global visited

    visited[node] = True
    queue = deque([node])
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
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a][b] = True
    graph[b][a] = True

answer = solution(1)

print(answer)