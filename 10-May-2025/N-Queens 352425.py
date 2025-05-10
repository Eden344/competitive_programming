# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(positions):
           
            board = []
            for i in range(n):
                row = ['.' * n]
                row = list(row[0])
                row[positions[i]] = 'Q'
                board.append(''.join(row))
            return board
        
        def is_safe(row, col, queens):
            for prev_row, prev_col in enumerate(queens[:row]):
                if prev_col == col:
                    return False
                if abs(prev_row - row) == abs(prev_col - col):
                    return False
            return True
        
        def backtrack(row, queens):
            if row == n:
                res.append(create_board(queens))
                return
            
            for col in range(n):
                if is_safe(row, col, queens):
                    queens[row] = col
                    backtrack(row + 1, queens)
                    queens[row] = 0
        
        res = []
        queens = [0] * n  
        backtrack(0, queens)
        return res