def solution(n):
    if n in [4, 7]:
        return (-1)
    
    if n % 5 == 0:
        return (n//5)

    if n == 3:
        return 1
    if n == 6:
        return 2
    if n == 8:
        return 2
    if n == 9:
        return 3

    posibility = {
        11 : 3,
        12 : 4,
        13 : 3,
        14 : 4,
        15 : 3,
        16 : 4,
        17 : 5,
        18 : 4,
        19 : 5,
    }

    cnt = 0

    while n > 20:
        n -= 5
        cnt += 1

    cnt += posibility[n]

    return (cnt)

n = int(input())

print(solution(n))