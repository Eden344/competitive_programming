# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty.append((i,j))
                else:
                    rows[i].add(val)
                    col[j].add(val)
                    box_id =  (i // 3) * 3 + (j // 3)
                    boxes[box_id].add(val)


        def backtrack(index):
            if index == len(empty):
                return True
            r,c = empty[index]
            box_id =  (r // 3) * 3 + (c // 3)

            for num in map(str, range(1,10)):
                if num not in rows[r] and num not in col[c] and num not in boxes[box_id]:
                    board[r][c] = num
                    rows[r].add(num)
                    col[c].add(num)
                    boxes[box_id].add(num)

                    if backtrack(index + 1):
                        return True
                    board[r][c] ="."
                    rows[r].remove(num)
                    col[c].remove(num)
                    boxes[box_id].remove(num)
            return False
        backtrack(0)



        