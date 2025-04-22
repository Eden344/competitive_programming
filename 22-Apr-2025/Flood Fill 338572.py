# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        moves = [(0,1),(1,0),(-1,0),(0,-1)]

        def inbound(row,col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        
        strt_clr = image[sr][sc]
        
        if strt_clr == color:
            return image
        
        que = deque()
        que.append((sr,sc))

        while que:
           
            row,col = que.popleft()
            image[row][col] = color

            for x,y in moves:
                n_row = row + x
                n_col = col + y
                if inbound(n_row,n_col) and image[n_row][n_col] == strt_clr:
                    
                    que.append((n_row,n_col))
        return image
        
        