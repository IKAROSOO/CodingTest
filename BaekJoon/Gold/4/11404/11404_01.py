import sys, heapq

input = sys.stdin.readline

n = int(input());   m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

for start_node in range(1, n+1):
    distance = [float('inf')] * (n+1)
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
    
    for i in range(1, n+1):
        if distance[i] == float('inf'):
            print(0, end= " ")
        else:
            print(distance[i], end= " ")
    print()


'''
해당 방법은 '다익스트라 알고리즘'을 N번 실행하는 방법
시간복잡도에서는 불리
'''