def solution(s):
    check_stack = list()
    n = len(s)

    if s[0] == ")":
        return False

    for i in range(n):
        if s[i] == "(":
            check_stack.append(1)
        else:
            if check_stack:
                check_stack.pop()
            else:
                return False
    
    if check_stack:
        return False

    return True