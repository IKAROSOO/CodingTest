n = int(input())
time_list = list(map(int, input().split(" ")))

time_list = sorted(time_list)
cnt = 0

for i in range(n):
    cnt += (n-i)*time_list[i]

print(cnt)

'''
2025_06_10_11:38
'''