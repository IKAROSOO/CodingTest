def solution(n):
    answer = []
    
    if is_prime(n):
        answer.append(n)
        return answer

    for i in range(2, int(n**0.5)+1):
        if n%i == 0 and is_prime(i):
            answer.append(i)
            print(i)
    
    return answer

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    
    return True