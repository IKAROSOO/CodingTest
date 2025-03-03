def solution(s):
    n = len(s)
    answer = []

    for i in range(n):
        if not answer:
            answer.append(s[i])
            continue

        if answer[-1] == '(':
            if s[i] == ')':
                answer.pop()
            else:
                answer.append(s[i])
        else:
            answer.append(s[i])
    
    if not answer:
        return True
    
    return False