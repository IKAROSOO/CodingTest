n = int(input())
ary = []

for i in range(n):
    ary.append((int(input()), i))

Max = 0
ary.sort()

for i in range(n):
    if Max < ary[i][1] - i:
        Max = ary[i][1] - i

print(Max + 1)

'''
잘 모르겠음
'''