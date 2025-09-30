# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp (i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            
            memo[i] = min(dp(i + 1) , dp(i + 2) ) + cost[i]
            return memo[i]
        return min(dp(0), dp(1))
        