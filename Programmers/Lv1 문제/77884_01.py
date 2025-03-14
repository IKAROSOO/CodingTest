def solution(left, right):
    '''left부터 right까지의 모든 수들 중에서,
    약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return'''

    answer = 0

    for num in range(left, right+1):
        if is_prime(num):
            answer += num
        elif is_squared(num):
            answer -= num
        else:
            answer += num
    
    return answer

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def is_squared(n):
    if n**0.5 == int(n**0.5):
        return True
    
    return False