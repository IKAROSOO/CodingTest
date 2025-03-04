def solution(my_string):
    answer = ""

    for char in my_string:
        if ord(char) >= 97:
            answer += chr(ord(char) - 32)
        else:
            answer += chr(ord(char) + 32)
    
    return answer