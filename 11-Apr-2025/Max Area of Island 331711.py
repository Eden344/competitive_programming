# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moves =[(1,0), (0,1), (0,-1), (-1,0)]
        visited = set()

        def inbound(row, col):
            return(0 <= row < len(grid) and 0 <= col < len(grid[0]))

        
        def dfs(row, col):

            if not inbound(row, col) or (row, col) in visited or grid[row][col] == 0:
                return 0
            else:
                ans = 1

            visited.add((row,col))

            for x, y in moves:
                n_row = row + x
                n_col = col + y
                if inbound(n_row, n_col) and grid[n_row][n_col] == 1:
                    ans += dfs(n_row, n_col)
            return ans


        maxi = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxi = max(maxi, dfs(i,j))
        return maxi

        