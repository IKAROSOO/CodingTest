n = int(input())

result = 0
cnt = 1

while cnt != n+1:
    for i in range(1, n+1):
        if cnt%i == 0:
            result += i
            print(i)
    cnt += 1

print(result)

'''
시간복잡도 : O(n^2)
'''