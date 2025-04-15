# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(0,1), (1,0),(-1,0),(0,-1)]

        def inbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        que = deque()

        one_cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    one_cnt += 1
                elif grid[i][j] == 2:
                    que.append([i,j])
        

        time = 0

        while que and one_cnt > 0:
            n = len(que)

           

            for _ in range(n):
                row,col = que.popleft()

                for x,y in moves:
                    n_row = row + x
                    n_col = col + y

                    if inbound(n_row, n_col) and grid[n_row][n_col] == 1:
                    
                        grid[n_row][n_col] = 2
                        que.append([n_row,n_col])
                        one_cnt -= 1
            time += 1


        if one_cnt == 0:
            return time
        else:
            return -1
            


        