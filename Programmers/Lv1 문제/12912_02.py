def solution(a, b):
    a, b = min(a, b), max(a, b)

    return (b*(b+1) - (a)*(a-1)) / 2