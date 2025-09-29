# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp (rem):
            if rem == 0:
                return 0
            elif rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]

            maxi = float('inf')
            for coin in coins:
                maxi = min(maxi, dp(rem - coin) + 1)
            memo[rem] = maxi
            return maxi
        res = dp(amount)
        if res != float("inf"):
            return res
        else:
            return -1
    


        