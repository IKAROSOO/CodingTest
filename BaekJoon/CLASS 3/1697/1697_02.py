from collections import deque

def bfs(start):
    global graph, visited

    queue = deque([(start, 0)])

    visited[start] = True

    while queue:
        node, cnt = queue.popleft()

        if node == k:
            return cnt
        
        next_nodes = [node-1, node+1, 2*node]

        for next in next_nodes:
            if 0 <= next < (2*(k+1)) and not visited[next]:
                visited[next] = True
                queue.append((next, cnt+1))

n, k = map(int, input().split())

graph = [0] * (2*(k+1))
visited = [False] * (2*(k+1))

answer = bfs(n)

print(answer)

'''
2025_08_31_19:26
다시 풀어본 것
해당 문제는 BFS로 푸는 것이 좋다.
'''