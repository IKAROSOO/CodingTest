N, M = map(int, input().split())
Paper = []

for i in range(N):
    rows = list(map(int, input().split()))
    Paper.append(rows)

def Shape01(List, N, M):        # 1자 모양
    sum_1 = 0
    sum_2 = 0

    for i in range(N):          # 가로인 경우
        for j in range(M - 3):
            sum = List[i][j] + List[i][j+1] + List[i][j+2] + List[i][j+3]
            sum_1 = max(sum, sum_1)

    for j in range(M):          # 세로인 경우
        for i in range(N - 3):
            sum = List[i][j] + List[i+1][j] + List[i+2][j] + List[i+3][j]
            sum_2 = max(sum, sum_2)
    
    return max(sum_1, sum_2)

def Shape02(List, N, M):        # ㅁ자 모양
    sum_0 = 0

    for i in range(N-1):
        for j in range(M-1):
            sum = List[i][j] + List[i+1][j] + List[i][j+1] + List[i+1][j+1]
            sum_0 = max(sum, sum_0)
    
    return sum_0

def Shape03(List, N, M):        # L자 모양
    sum0 = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0

    for i in range(N-2):        # Case 1
        for j in range(M-1):
            sum = List[i][j] + List[i+1][j] + List[i+2][j] + List[i+2][j+1]
            sum0 = max(sum, sum0)
    
    for i in range(1, N):       # Case 2
        for j in range(M-2):
            sum = List[i][j] + List[i][j+1] + List[i][j+2] + List[i-1][j+2]
            sum1 = max(sum, sum1)
    
    for i in range(N-2):        # Case 3
        for j in range(M-1):
            sum = List[i][j] + List[i][j+1] + List[i+1][j+1] + List[i+2][j+1]
            sum2 = max(sum, sum2)
    
    for i in range(N-1):          # Case 4
        for j in range(M-2):
            sum = List[i][j] + List[i+1][j] + List[i][j+1] + List[i][j+2]
            sum3 = max(sum, sum3)
    
    for i in range(2, N):           # Case 5
        for j in range(M-1):
            sum = List[i][j] + List[i][j+1] + List[i-1][j+1] + List[i-2][j+1]
            sum4 = max(sum, sum4)
    
    for i in range(N-1):            # Case 6
        for j in range(M-2):
            sum = List[i][j] + List[i][j+1] + List[i][j+2] + List[i+1][j+2]
            sum5 = max(sum, sum5)

    for i in range(N-2):            # Case 7
        for j in range(M-1):
            sum = List[i][j] + List[i][j+1] + List[i+1][j] + List[i+2][j]
            sum6 = max(sum, sum6)

    for i in range(N-1):
        for j in range(M-2):
            sum = List[i][j] + List[i+1][j] + List[i+1][j+1] + List[i+1][j+2]
            sum7 = max(sum, sum7)

    return max(sum0, sum1, sum2, sum3, sum4, sum5, sum6, sum7)

def Shape04(List, N, M):        # ㄹ자 모양
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    for i in range(N-2):
        for j in range(M-1):
            sum = List[i][j] + List[i+1][j] + List[i+1][j+1] + List[i+2][j+1]
            sum1 = max(sum, sum1)
    
    for i in range(1, N):
        for j in range(M-2):
            sum = List[i][j] + List[i][j+1] + List[i-1][j+1] + List[i-1][j+2]
            sum2 = max(sum, sum2)
    
    for i in range(N-2):
        for j in range(1, M):
            sum = List[i][j] + List[i+1][j] + List[i+1][j-1] + List[i+2][j-1]
            sum3 = max(sum, sum3)

    for i in range(N-1):
        for j in range(M-2):
            sum = List[i][j] + List[i][j+1] + List[i+1][j+1] + List[i+1][j+2]
            sum4 = max(sum, sum4)
    
    return max(sum1, sum2, sum3, sum4)

def Shape05(List, N, M):        # ㅗ자 모양
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    for i in range(1, N):
        for j in range(M-2):
            sum = List[i][j] + List[i][j+1] + List[i][j+2] + List[i-1][j+1]
            sum1 = max(sum, sum1)
    
    for i in range(N-2):
        for j in range(M-1):
            sum = List[i][j] + List[i+1][j] + List[i+1][j+1] + List[i+2][j]
            sum2 = max(sum, sum2)

    for i in range(N-1):
        for j in range(M-2):
            sum = List[i][j] + List[i][j+1] + List[i][j+2] + List[i+1][j+1]
            sum3 = max(sum, sum3)
    
    for i in range(1, N-1):
        for j in range(M-1):
            sum = List[i][j] + List[i][j+1] + List[i-1][j+1] + List[i+1][j+1]
            sum4 = max(sum, sum4)

    return max(sum1, sum2, sum3 ,sum4)

ans = max(Shape01(Paper, N, M), Shape02(Paper, N, M), Shape03(Paper, N, M),
          Shape04(Paper, N, M), Shape05(Paper, N, M))

print(ans)