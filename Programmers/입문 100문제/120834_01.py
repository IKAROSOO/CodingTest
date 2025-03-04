def solution(age):
    answer = ''

    ageStr = str(age)

    for i in range(len(ageStr)):
        age1 = int(ageStr[i]) + 97
        ageAscii = chr(age1)

        answer += ageAscii
    
    return answer