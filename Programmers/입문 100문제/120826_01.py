def solution(my_string, letter):
    answer = ""

    for alphabet in my_string:
        if alphabet == letter:
            continue
        answer += alphabet

    return answer