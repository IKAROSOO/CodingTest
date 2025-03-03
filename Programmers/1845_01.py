def solution(nums):
    n = len(nums)
    mine = n//2

    guide = {}

    for pocketmon_num in nums:
        if pocketmon_num not in guide:
            guide[pocketmon_num] = 0
        guide[pocketmon_num] += 1

    if mine >= len(guide):
        return len(guide)
    else:
        return mine