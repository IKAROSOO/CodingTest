n = int(input())
ary = [int(input()) for i in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if ary[j] > ary[j+1]:
            temp = ary[j]
            ary[j] = ary[j+1]
            ary[j+1] = temp

for i in range(n):
    print(ary[i])


'''
잘 모르겠음
'''