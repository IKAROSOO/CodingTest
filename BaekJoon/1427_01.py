num = list(input())
n = len(num)

for i in range(n):
    num[i] = int(num[i])

for i in range(n):
    Max = i
    for j in range(i+1, n):
        if num[j] > num[Max]:
            Max = j
    if num[i] < num[Max]:
        temp = num[i]
        num[i] = num[Max]
        num[Max] = temp
    
for i in range(n):
    print(num[i])