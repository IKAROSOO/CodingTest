class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        cnt = 0

        while cnt != k:
            min_num = min(nums)
            min_num_index = nums.index(min_num)

            nums[min_num_index] = min_num * multiplier

            cnt += 1

        return nums