def solution(my_string, n):
    answer = ""

    for string in range(len(my_string)):
        for repeat in range(n):
            answer += my_string[string]

    return answer