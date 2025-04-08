# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        moves = [(1,0), (0,1), (0,-1), (-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs ( row, col):
            if not inbound(row,col) or grid[row][col] == 0:
                return 1

            if visited[row][col]:
                return 0

            visited[row][col] = True
            primeter = 0

            for x, y in moves:
                primeter += dfs (row + x, col + y)
            return primeter


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)

        return 0    
