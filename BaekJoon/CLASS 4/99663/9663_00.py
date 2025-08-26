def solution(row):
    global cnt

    if row == n:
        cnt += 1
        return
    
    for col in range(n):
        if col_check[col] or diag1_check[row+col] or diag2_check[(row-col) + (n-1)]:
            continue

        col_check[col] = True
        diag1_check[row + col] = True
        diag2_check[(row-col) + (n-1)] = True

        solution(row+1)

        col_check[col] = False
        diag1_check[row + col] = False
        diag2_check[(row-col) + (n-1)] = False

n = int(input())
cnt = 0

col_check = [False] * n
diag1_check = [False] * (2*n - 1)
diag2_check = [False] * (2*n - 1)

solution(0)

print(cnt)

'''
제미나이가 풀어준 코드
다시 풀어볼 필요 있음
'''