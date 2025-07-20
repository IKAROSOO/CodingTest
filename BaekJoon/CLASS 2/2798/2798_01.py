n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = cards[i] + cards[j] + cards[k]

            if tmp <= m:
                cnt = max(tmp, cnt)

print(cnt)