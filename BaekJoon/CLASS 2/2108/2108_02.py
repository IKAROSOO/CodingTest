import sys
input = sys.stdin.readline

n = int(input())

nums = list()
nums_dict = dict()
for _ in range(n):
    num = int(input())

    if num not in nums_dict:
        nums_dict[num] = 0
    
    nums_dict[num] += 1
    nums.append(num)

# 산술평균 계산
avg = round(sum(nums) / n)

# 중앙값 계산
nums.sort()
mid = nums[n//2]

# 최빈값 계산
nums_dict = list(sorted(nums_dict.items(), key=lambda x: (-x[1], x[0])))

if len(nums_dict) >= 2 and nums_dict[0][1] == nums_dict[1][1]:
    most = nums_dict[1][0]
else:
    most = nums_dict[0][0]

# 범위 계산
range = max(nums) - min(nums)

print(avg)
print(mid)
print(most)
print(range)