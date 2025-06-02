def solution(prices):
    n = len(prices)
    answer = list(0 for _ in range(n))
    stack = list()

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1

    return answer