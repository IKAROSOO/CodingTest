class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        volume = 0

        while left < right:
            width = right - left
            top = min(height[left], height[right])

            volume = max(volume, width*top)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return (volume)