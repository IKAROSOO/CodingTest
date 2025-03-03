def solution(box, n):
    diceCnt = 1

    for edge in box:
        cnt = edge//n

        diceCnt *= cnt
    
    return diceCnt