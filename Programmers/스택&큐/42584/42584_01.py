def solution(prices):
    n = len(prices)
    answer = list()

    for i in range(n):
        standard = prices[i]
        cnt = 1
        j = i
        while True:
            i += 1
            
            try:
                if standard > prices[i]:
                    answer.append(cnt)
                    break
            except:         # i가 prices의 index를 초과하는 경우
                answer.append(n - (j+1))
                break

            cnt += 1
        
    return answer