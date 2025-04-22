# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        moves = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
        def inbound(row,col):
            return(0 <= row < len(board) and 0 <= col < len(board[0]))
        def mine_cnt(row,col):
            mine = 0
            for x,y in moves:
                n_row = row + x
                n_col = col + y
                if inbound(n_row,n_col) and board[n_row][n_col] == "M":
                    mine += 1
            return mine

        r,c = click
        if board[r][c] == "M":
            board[r][c] ="X"
            return board
        
        que = deque([(r,c)])
       
        visited = set()
        visited.add((r,c))

        while que:
           
            row,col = que.popleft()
            mines = mine_cnt(row,col)
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] ="B"
                for x,y in moves:
                    n_row = row + x
                    n_col = col + y
                    if inbound(n_row,n_col) and board[n_row][n_col] == "E" and (n_row,n_col) not in visited:
                        que.append((n_row,n_col))
                        visited.add((n_row,n_col))
               
        return board






        

        