def solution(num1, den1, num2, den2):
    answer = []

    num = num1*den2 + num2*den1
    den = den1*den2

    gcd = GCD(num, den)

    answer.extend([num//gcd, den//gcd])

    return answer

def GCD(a, b):
    while(b > 0):
        a, b = b, a%b
    return a

'''
유클리드 알고리즘을 사용한 코드이다.

GCD는 최대공약수를 구할 수 있게 해주는 함수이다.
'''