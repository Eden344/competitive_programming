# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        for i in range( n -1, -1, -1):
            for cap in range(W + 1):
                exclude = dp[i + 1][cap]
                include = 0
                if cap >= wt[i]:
                    include = dp[i + 1] [cap - wt[i]] + val[i]
                dp[i][cap] = max(include,exclude)
        return dp[0][W]