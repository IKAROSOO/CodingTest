N = int(input())
num = list(map(int, input().split()))
num.sort()

cnt = 0

for n in range(N):
    find = num[n]
    left, right = 0, N-1

    while left < right:
        if num[left] + num[right] == find:
            if left != n and right != n:
                cnt += 1
                break
            elif left == n:
                left += 1
            elif right == n:
                right -= 1
        elif num[left] + num[right] < find:
            left += 1
        else:
            right -= 1

print(cnt)