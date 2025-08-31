def back_Tracking(curr, n, k, cost, min_c, graph, check):
    if cost > k:
        return
    
    check.add(curr)

    for node in range(1, n+1):
        cost_edge = graph[curr][node]

        if cost_edge:
            new_cost = cost + cost_edge

            if new_cost <= k and new_cost < min_c[node]:
                min_c[node] = new_cost
                back_Tracking(node, n, k, new_cost, min_c, graph, check)

def solution(n, roads, k):
    check = set()
    graph = [[0] * (n+1) for _ in range(n+1)]

    for u, v, c in roads:
        if not graph[u][v] or c < graph[u][v]:
            graph[u][v] = c
            graph[v][u] = c
        
    min_c = [float("inf")] * (n+1)
    min_c[1] = 0

    back_Tracking(1, n, k, 0, min_c, graph, check)

    return len(check)