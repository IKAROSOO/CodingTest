class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp1 = 1
        dp2 = 2
        dpn = 0

        for _ in range(3, n+1):
            dpn = dp1 + dp2

            dp1 = dp2
            dp2 = dpn
    
        return dpn

'''
시간복잡도와 공간복잡도를 동시에 고려한 DP(동적계획법) 문제
'''