from collections import deque

def solution(start):
    global visited

    max_limit = 2*(max(n, k)+2)
    queue = deque([(start, 0)])

    while queue:
        node, cnt = queue.popleft()

        if node == k:
            return cnt

        next_node = [node+1, node-1, 2*node]

        for next in next_node:
            if 0<= next < max_limit and not visited[next]:
                visited[next] = True
                queue.append((next, cnt+1))
    
    return -1

n, k = map(int, input().split())

line = list(0 for _ in range(max(n, k)+1))
visited = [False]*(2*(max(n,k)+2))

answer = solution(n)
print(answer)