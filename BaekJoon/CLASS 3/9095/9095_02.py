def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return solution(n-1) + solution(n-2) + solution(n-3)

T = int(input())

for _ in range(T):
    n = int(input())

    print(solution(n))

'''
2025_07_18_15:40
'''