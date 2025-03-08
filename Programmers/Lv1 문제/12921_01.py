def solution(n):
    '''1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수'''

    prime_list = []

    for i in range(1, n+1):
        if is_Prime(i):
            prime_list.append(i)
    
    return len(prime_list)

def is_Prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int((n**0.5))+1):
        if n % i == 0:
            return False
    
    return True

'''
시간 복잡도 : O(n√n)
'''