import sys
import heapq

input = sys.stdin.readline

n = int(input());   m = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
distance = [float('inf')] * (n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())

    graph[start].append((end, cost))

start_node, target_node = map(int, input().split())
distance[start_node] = 0

pq = [(0, start_node)]

while pq:
    dist, cur_node = heapq.heappop(pq)

    if distance[cur_node] < dist:
        continue

    for neighbor, cost in graph[cur_node]:
        new_dist = dist + cost

        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

print(distance[target_node])