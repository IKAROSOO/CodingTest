n = int(input())
ary = []

for i in range(n):
    row = input()
    ary.append(row)

'''
C : Red
P : Blue
Z : Green
Y : Yellow
'''

change_cnt = 0

for i in range(n-1):
    for j in range(n-1):
        if ary[i][j] != ary[i+1][j]:
            change_cnt += 1
        if ary[i][j] != ary[i][j+1]:
            change_cnt += 1
if ary[-1][-1] != ary[-2][-1]:
    change_cnt += 1
if ary[-1][-1] != ary[-1][-2]:
    change_cnt += 1

candy_max = 0
try_cnt = 0

while change_cnt > try_cnt:
    
    try_cnt += 1