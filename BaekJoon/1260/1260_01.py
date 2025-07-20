import sys
input = sys.stdin.readline

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=" ")

    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=" ")

        for next in range(1, n+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)

# 1. 기본 입력 및 초기화
n, m, v = map(int, input().split())

graph = list([False] * (n+1) for _ in range(n+1))
visited = list([False] * (n+1))

# 2. 그래프 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(v)
print()

visited = list([False] * (n+1))
q = [v]
visited[v] = True

bfs()