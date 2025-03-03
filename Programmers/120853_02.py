def solution(s):
    stack = []

    for element in s.split():
        if element == "Z":
            stack.pop()
        else:
            stack.append(int(element))
    
    return sum(stack)