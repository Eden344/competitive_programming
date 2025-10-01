# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(i,j):
            if i == len(triangle) - 1:
                return triangle[i][j] 
            if (i,j) in memo:
                return memo[(i,j)]
            down_right = dp(i + 1,j)
            down_left = dp(i + 1, j + 1)

            memo[(i,j)] = triangle[i][j]  + min(down_right, down_left)
            return memo[(i,j)]
           
        return dp(0,0)

        