n, money = map(int, input().split(" "))
coin_list = list()
cnt = 0

for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

idx = n-1

while money:
    if money//coin_list[idx] >= 1:
        tmp = money // coin_list[idx]
        
        money -= tmp*coin_list[idx]
        cnt += tmp
        continue
    
    idx -= 1

print(cnt)