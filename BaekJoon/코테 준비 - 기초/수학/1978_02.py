n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for num in nums:
    k = 2
    verify = 0

    while num > k:
        if num%k != 0:
            verify += 1
        k+= 1
        
    if verify+2 == num:
            cnt += 1
        
print(cnt)

'''
O(n)보다는 크다. nums에서 제일 큰 숫자의 크기에 영향을 받음
'''