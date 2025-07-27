n = int(input())
inputs = list(map(int, input().split()))

unique = sorted(set(inputs))

compression = dict()
idx = 0

for num in unique:
    compression[num] = idx
    idx += 1

for num in inputs:
    print(compression[num], end=" ")