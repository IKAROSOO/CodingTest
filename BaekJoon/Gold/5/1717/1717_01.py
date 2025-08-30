import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    global parent

    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    global parent

    a_P, b_P = find(a), find(b)

    if a_P == b_P:
        return
    else:
        n_P = min(a_P, b_P)
        n_C = max(a_P, b_P)

        parent[n_C] = n_P

n, m = map(int, input().split())

parent = list(i for i in range(n+1))
cmd = list()

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