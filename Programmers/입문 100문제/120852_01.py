def solution(n):
    answer = []

    if is_prime(n):
        answer.append(n)
        return answer
    
    for num in range(2, n):
        if n % num == 0:
            if is_prime(num):
                answer.append(num)
    
    return answer

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    
    return True