def solution(nums):
    cnt = 0
    hash_map = dict()
    
    for num in nums:
        hash_map[num] = hash_map.get(num, 0)
    
    return min(len(hash_map), len(nums)//2)