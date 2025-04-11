# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        moves = [(0,1), (1,0),(0,-1),(-1,0)]
        visited = set()
        m = len(board)
        n = len(board[0])

        def inbound(row, col):
            return (0 <= row < m and 0 <= col < n)

        def dfs(row, col):
            board[row][col] = "#"
            
            visited.add((row,col))

            for x, y in moves:
                n_row = row + x
                n_col = col + y
                if inbound(n_row, n_col) and board[n_row][n_col] == "O":
                    dfs(n_row, n_col)     

        for i in range(m):
            for j in range(n):
                if i != 0 and  j != 0 and i != m - 1 and j != n -1:
                    continue               
                if board[i][j] == "O":
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"