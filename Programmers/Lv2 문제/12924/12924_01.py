def solution(n):
    answer = 0
    
    for i in range(1, n//2 + 1):
        cnt = 0
        for j in range(i, n//2 + 2):
            cnt += j
            
            if cnt == n:
                answer += 1
                break
            if cnt > n:
                break
    
    return answer+1