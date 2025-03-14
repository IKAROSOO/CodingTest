def solution(left, right):
    '''left부터 right까지의 모든 수들 중에서,
    약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return'''

    answer = 0

    for num in range(left, right+1):
        if is_squared(num):
            answer -= num
        else:
            answer += num
    
    return answer

def is_squared(n):
    if int(n**0.5) == n**0.5:
        return True
    
    return False