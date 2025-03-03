class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)

        ans = []

        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    
                    break
        
        return ans