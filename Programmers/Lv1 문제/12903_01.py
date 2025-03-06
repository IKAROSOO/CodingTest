def solution(s):
    n = len(s)

    if n%2 != 0:
        return "".join(s[n//2])
    else:
        return "".join(s[(n//2)-1 : (n//2+1)])