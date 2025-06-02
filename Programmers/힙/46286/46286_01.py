def solution(scoville, K):
    if min(scoville) >= K:
        return 0

    cnt = 1
    
    while True:
        if len(scoville) <= 1:
            return -1

        scoville.sort(reverse=True)
        x = scoville.pop()
        y = scoville.pop()

        scoville.append(x + 2*y)

        if min(scoville) < K:
            cnt += 1
            continue
        
        return cnt

'''
시간복잡도가 O(n^2log(n))이기 때문에 효율이 좋지 않음
'''