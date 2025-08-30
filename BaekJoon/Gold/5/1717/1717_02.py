import sys

input = sys.stdin.readline

def find(x):
    global parent

    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(a, b):
    global parent, size

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if size[root_a] < size[root_b]:
            parent[root_a] = root_b
            size[root_b] += size[root_a]
        else:
            parent[root_b] = root_a
            size[root_a] += size[root_b]

n, m = map(int, input().split())

parent = list(i for i in range(n+1))
size = [1]*(n+1)

for _ in range(m):
    x, a, b = map(int, input().split())
    
    if not x:
        union(a, b)
        continue
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")