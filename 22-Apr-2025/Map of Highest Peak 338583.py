# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        que = deque()
        ans = [[-1] * len(isWater[0]) for _ in range(len(isWater))]

        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(row,col):
            return (0 <= row < len(isWater) and 0 <= col < len(isWater[0]))
        
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    que.append((i,j))
                
        while que:
          
            row,col= que.popleft()

            for x,y in moves:
                n_row = row + x
                n_col = col + y
                if inbound(n_row,n_col) and ans[n_row][n_col] == -1:
                    ans[n_row][n_col] = ans[row][col] + 1
                    que.append((n_row,n_col))
        
        return ans

        