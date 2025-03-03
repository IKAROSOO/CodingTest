A, B = map(int, input().split())
A, B = str(A), str(B)

new_A = A[::-1]
new_B = B[::-1]

new_A, new_B = int(new_A), int(new_B)

print(max(new_A, new_B))