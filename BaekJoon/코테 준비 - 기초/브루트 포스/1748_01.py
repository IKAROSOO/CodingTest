N = int(input())

i = 1
cnt = 0

while N // (10**i) != 0:
    i += 1

for a in range(i-1):
    cnt += ((10 ** (a+1)) - (10 ** a)) * (a+1)

cnt += (N-(10**(i-1))+1)*i

print(cnt)