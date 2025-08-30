import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = list(float('inf') for _ in range(n+1))
        distance[k] = 0

        graph = [[] for _ in range(n+1)]

        for start, end, time in times:
            graph[start].append((end, time))

        pq = [(0, k)]

        while pq:
            dist, cur_node = heapq.heappop(pq)

            if distance[cur_node] < dist:
                continue

            for neighbor, cost in graph[cur_node]:
                new_dist = dist + cost

                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        

        distance = distance[1:]
        max_dist = max(distance)

        if max_dist == float('inf'):
            return -1
        else:
            return max_dist