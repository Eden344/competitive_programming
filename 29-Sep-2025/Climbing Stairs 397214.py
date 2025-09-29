# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp (m):
            if m == 0 or m == 1:
                return 1
            if m not in memo:
                memo[m] = dp(m -1) + dp(m - 2)

            return (memo[m])
        return dp(n)
        
        