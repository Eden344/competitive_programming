# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = [(0,1), (1,0)]
        memo = defaultdict(int)
        
       
        def dfs(i,j):
            if i == m -1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0

            if (i,j) not in memo:   
                right = dfs(i, j+1)
                down = dfs(i+1, j)
                memo[(i,j)] = right + down

            return memo[(i,j)]
            
        return dfs(0,0)



        
        