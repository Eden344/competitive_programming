# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        moves = {
            1: [(0,1),(0,-1)],
            2: [(1,0),(-1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }

        opp = {
            (0,-1):(0,1),
            (0,1):(0,-1),
            (-1,0):(1,0),
            (1,0):(-1,0)
        }

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        visited = [[False] * n for _ in range(m)]
        que = deque()
        que.append((0, 0))
        visited[0][0] = True

        while que:
            x, y = que.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            for dx, dy in moves[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if inbound(nx, ny) and not visited[nx][ny]:
                    if opp[(dx, dy)] in moves[grid[nx][ny]]:
                        visited[nx][ny] = True
                        que.append((nx, ny))
        return False
