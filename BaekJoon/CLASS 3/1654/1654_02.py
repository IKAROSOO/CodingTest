k, n = map(int, input().split())
cables = list()

for _ in range(k):
    cables.append(int(input()))

left, right = 1, max(cables)
answer = 0

while left <= right:
    cnt = 0
    middle = (left+right)//2

    for cable in cables:
        cnt += cable//middle
    
    if cnt < n:
        right = middle - 1
    else:
        left = middle + 1
        answer = middle
    
print(answer)

'''
2025_08_25_21:25
'''