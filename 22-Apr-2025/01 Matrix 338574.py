# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        que = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    que.append((r, c, 0))
                    visited.add((r, c))

        while que:
            row, col, path = que.popleft()
            for dx, dy in moves:
                n_row, n_col = row + dx, col + dy
                if 0 <= n_row < rows and 0 <= n_col < cols and (n_row, n_col) not in visited:
                    mat[n_row][n_col] = path + 1
                    visited.add((n_row, n_col))
                    que.append((n_row, n_col, path + 1))

        return mat
