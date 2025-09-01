class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    
'''
함수의 원리는 이해했지만, 해당 input자체가 아직 헷갈림
다시 풀어볼 필요 있음
'''