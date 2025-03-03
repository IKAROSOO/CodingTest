def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isPrime(nums[i]+nums[j]+nums[k]):
                    answer += 1
                    print(nums[i]+nums[j]+nums[k])

    return answer

# 소수면 Ture, 아니면 False
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True