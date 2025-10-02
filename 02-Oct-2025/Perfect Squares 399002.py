# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        sqr = []
        for i in range(1, n + 1):
            if sqrt(i).is_integer():
                sqr.append(i)
        print(sqr)
        
        memo = {}
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf")
            if rem in memo:
                return memo[rem]

            maxi = float('inf')
            for sq in sqr:
                maxi = min(maxi, dp(rem - sq) + 1)
            memo[rem] = maxi
            return maxi


        res = dp(n)
        if res != float("inf"):
            return res
        