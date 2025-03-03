def function_A(n):
    nums = []
    
    for i in range(1, n+1):
        if n%i == 0:
            nums.append(i)
    
    return sum(nums)

n = int(input())
result = 0
cnt = 1

while cnt != n:
    result += function_A(cnt)
    cnt += 1

result += function_A(n)

print(result)

'''
시간초과이므로 다시 코드 작성 필요

시간복잡도 : O(n^2)
'''