def solution(n):
    '''1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수'''

    if n < 2:
        return 0
    
    primes = [True] * (n+1)
    # 소수 여부를 저장하는 리스트
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    return sum(primes)

'''
시간 복잡도 : O(nloglogn)
'''