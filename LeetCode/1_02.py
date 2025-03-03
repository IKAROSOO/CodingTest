class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}
        for i,n in enumerate(nums):
            if n in subs.keys():
                return [i, subs[n]]
            subs[target - n] = i