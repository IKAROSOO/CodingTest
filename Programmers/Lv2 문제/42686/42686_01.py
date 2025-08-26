import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K:
        food1, food2 = heapq.heappop(scoville), heapq.heappop(scoville)
        new = food1 + (food2*2)

        heapq.heappush(scoville, new)

        cnt += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return cnt