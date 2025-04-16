# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        def inbound(row,col):
            return(0 <= row <len(maze) and 0 <= col < len(maze[0]))
        
        que = deque([(entrance[0],entrance[1], 0)])
        visited = set()
        visited.add((entrance[0],entrance[1]))

        while que:
            row,col,path = que.popleft()
            if (row == 0 or col == 0 or row == len(maze) -1 or col == len(maze[0]) - 1) and (row,col) != tuple(entrance):
                return path
            

            for x,y in moves:
                n_row = row + x
                n_col = col + y
                if inbound(n_row,n_col) and maze[n_row][n_col] == "." and (n_row,n_col) not in visited:
                    visited.add((n_row,n_col))
                    que.append((n_row,n_col,path + 1))
        return -1




