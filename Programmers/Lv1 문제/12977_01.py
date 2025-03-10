def solution(nums):
    '''주어진 숫자 배열에서 서로 다른 3개의 숫자를 더했을 때
    소수가 되는 경우의 수를 구하는 문제'''

    cnt = 0
    nums.sort()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    cnt += 1
    
    return cnt

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True