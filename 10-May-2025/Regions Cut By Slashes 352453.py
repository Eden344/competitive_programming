# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                c = grid[i][j]

                if c == '/':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif c == '\\':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:  
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)

                if i + 1 < n:
                    bottom = root + 2
                    top = 4 * ((i + 1) * n + j) + 0
                    union(bottom, top)
                if j + 1 < n:
                    right = root + 1
                    left = 4 * (i * n + j + 1) + 3
                    union(right, left)

        return sum(i == find(i) for i in range(4 * n * n))
