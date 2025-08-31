def solution(N, road, K):
    town = [[float("inf")] * (N+1) for _ in range(N+1)]

    for r in road:
        a, b, c = r

        if c < town[a][b]:
            town[a][b] = c
            town[b][a] = c

    distance = [float("inf")] * (N+1)
    distance[1] = 0

    visited = [False] * (N+1)

    for _ in range(N):
        min_dist = float("inf")
        node = -1

        for i in range(1, N+1):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                node = i

        if node == -1:
            break

        visited[node] = True

        for i in range(1, N+1):
            new_dist = distance[node] + town[node][i]

            if new_dist < distance[i]:
                distance[i] = new_dist
    cnt = 0

    for i in range(1, N+1):
        if distance[i] <= K:
            cnt += 1
    
    return cnt