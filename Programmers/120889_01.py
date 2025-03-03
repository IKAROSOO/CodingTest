def solution(sides):
    sides.sort()
    longest = sides.pop()

    if longest >= sum(sides):
        return 2
    else:
        return 1