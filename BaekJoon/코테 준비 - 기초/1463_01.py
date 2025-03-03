n = int(input())

cnt = 0

while(n != 1):
    if n%3 == 0:
        n = int(n/3)
        print(n)
        cnt += 1
        continue

    if n%2 == 0:
        n = int(n/2)
        print(n)
        cnt += 1
        continue
    
    n -= 1
    print(n)

    cnt += 1


print(cnt)