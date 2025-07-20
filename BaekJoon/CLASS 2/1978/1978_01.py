def solution(n):
    flag = False

    if n == 1:
        return 0

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            flag = True
            break
    else:
        return 1

    if flag:
        return 0
        

n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for num in nums:
    cnt += solution(num)

print(cnt)