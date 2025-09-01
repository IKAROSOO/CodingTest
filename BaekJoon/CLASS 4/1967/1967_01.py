import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    distance = [-1] * (n+1)
    distance[start] = 0

    queue = deque([(start, 0)])

    max_dist = 0
    far_node = start

    while queue:
        node, cnt = queue.popleft()

        for next, weight in graph[node]:
            if distance[next] == -1:
                dist = cnt + weight
                distance[next] = dist
                queue.append((next, dist))

                if max_dist < dist:
                    max_dist = dist
                    far_node = next

    return max_dist, far_node

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())

    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

_, far_node = bfs(1)
answer, _ = bfs(far_node)

print(answer)

'''
해당 문제를 BFS로 풀어야겠다는 발상을 하지 못했음.
다시 풀어봐야 함
'''