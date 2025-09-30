# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        moves  = [(0,1), (1,0)]
        memo = defaultdict(int)

        def dp(i,j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if i >= len(grid) or j >= len(grid[0]):
                return math.inf
            
            if (i,j) not in memo:
                right = dp(i, j + 1) 
                down = dp(i + 1, j) 
                memo[(i,j)] = grid[i][j] + min(right , down)
            return memo[(i,j)]
        return dp(0,0)


            
            
        