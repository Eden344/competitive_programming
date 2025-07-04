# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        row = len(grid)
        col = len(grid[0])
        empty = 0
        sx,sy = 0,0

        def inbound(x,y):
            return(0<= x < row and 0 <= y < col)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    sx,sy = i,j
                elif grid[i][j] == 2:
                    empty += 1

        def dfs(x,y, remains):
            if not inbound(x,y) or grid[x][y] == -1:
                return 0

            if grid[x][y] == 2:
                return 1 if remains == 0 else 0

            temp = grid[x][y]
            grid[x][y] = -1  
            paths = 0

            for dx,dy in moves:
                nx = dx + x
                ny = dy + y
                paths += dfs(nx,ny,remains - 1)

            grid[x][y] = temp
            return paths
        return dfs(sx,sy,empty)


        