def solution(cipher, code):
    answer = ""

    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    
    return answer

# -> cipher[code-1::code]