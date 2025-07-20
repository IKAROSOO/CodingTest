import sys
input = sys.stdin.readline
n = int(input())
num_list = list()
num_dict = dict()
modes = list()

for _ in range(n):
    num = int(input())
    num_list.append(num)

    if num not in num_dict:
        num_dict[num] = 0

    num_dict[num] += 1

num_list.sort()

max_frequency = max(num_dict.values())

for num, freq in num_dict.items():
    if freq == max_frequency:
        modes.append(num)

modes.sort()

if len(modes) == 1:
    mode = modes[0]
else:
    mode = modes[1]

mean = round(sum(num_list)/n)
median = num_list[n//2]
range = max(num_list) - min(num_list)

print(mean)
print(median)
print(mode)
print(range)

'''
2025_07_07_13:36
'''