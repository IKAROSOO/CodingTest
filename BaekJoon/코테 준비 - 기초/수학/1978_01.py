n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for num in nums:
    if num < 2:
        continue

    is_Prime = True

    for i in range(2, num):
        if num%i == 0:
            is_Prime = False
            break

    if is_Prime:
        cnt += 1

print(cnt)