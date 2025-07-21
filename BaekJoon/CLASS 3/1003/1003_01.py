def solution(n):
    global cnt_0, cnt_1

    if n == 0:
        cnt_0 += 1
        return 1
    if n == 1:
        cnt_1 += 1
        return 1
    
    return solution(n-2) + solution(n-1)   

T = int(input())

for _ in range(T):
    n = int(input())
    cnt_0, cnt_1 = 0, 0

    solution(n)

    print(cnt_0, cnt_1)

'''
시간초과가 난다.
'''