import math

def solution(num1, den1, num2, den2):
    answer = []

    den = den1*den2
    num = num1*den2 + num2*den1
    
    gcd_value = math.gcd(num, den)

    den = den // gcd_value
    num = num // gcd_value

    answer.append(num)
    answer.append(den)

    # answer.extend([num, den]) 을 사용하면 한 번에 리스트에 추가하는 것이 가능하다.

    return answer