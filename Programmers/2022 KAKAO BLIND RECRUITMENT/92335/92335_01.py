def solution(n, k):
    cnt = 0
    convert_num = convert_base(n, k)
    num_list = convert_num.split("0")

    for num in num_list:
        if not num:         # 분리한 수가 공백인 경우 제외
            continue
        else:
            if isPrime(int(num)):
                cnt += 1
    
    return cnt

def convert_base(num, k):   # num을 k진법으로 바꾸는 함수

    baseK = ""

    while num//k > 0:       # 나머지가 몫이 0이상인 경우는 계속해서 연산산
        remain = num%k
        num //= k
        baseK += str(remain)    # 나머지를 저장
    baseK += str(num)           # 마지막 나머지 저장
    baseK = baseK[::-1]         # 저장된 수를 역순으로 저장

    return baseK

def isPrime(num):           # 소수인지 아닌지 판별하는 함수
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True