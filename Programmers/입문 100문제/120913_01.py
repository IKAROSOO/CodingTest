def solution(my_str, n):
    answer = []
    cnt = 0
    term = ""

    for i in range(len(my_str)):
        if cnt == n:
            answer.append(term)
            term = ""
            cnt = 0

        term += my_str[i]
        cnt += 1
    else:
        answer.append(term)
    
    return answer