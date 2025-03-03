def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if checkStartWith(phone_book[i], phone_book[j]):
                return False

    return True

def checkStartWith(num1, num2):
    min_len = min(len(num1), len(num2))

    for i in range(min_len):
        if num1[i] != num2[i]:
            return False

    return True