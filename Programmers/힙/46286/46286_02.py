import heapq

def solution(scoville, K):    
    cnt = 0
    
    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:
            return cnt

        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + 2*second

        heapq.heappush(scoville, new)

        cnt += 1

'''
GPT가 푼 방법
Heap을 써야하는 것은 알았지만, 이렇게 쓰는지는 몰랐다
'''