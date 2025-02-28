# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        mini = float('inf')
        first_robo = sum(grid[0])
        scnd_robo = 0

        for i in range(len(grid[0])):
            first_robo -= grid[0][i]
            mini = min(mini, max(first_robo,scnd_robo))
            scnd_robo += grid[1][i]
        return mini
        