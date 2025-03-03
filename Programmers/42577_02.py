def solution(phone_book):
    memo = {}

    for number in memo:
        memo[number] = 1

    for number in phone_book:
        for i, n in enumerate(number):
            if number[: i] in memo:
                return False
    
    return True

def checkStartWith(num1, num2):
    min_len = min(len(num1), len(num2))

    for i in range(min_len):
        if num1[i] != num2[i]:
            return False
    
    return True