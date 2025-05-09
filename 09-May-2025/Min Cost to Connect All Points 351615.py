# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            
            if parent[x] != x:
                return find(parent[x])
            return parent[x]


        def union(i, j):
            
            pi = find(i)
            pj = find(j)

            if pi != pj:
                if size[pi] > size[pj]:
                    parent[pj] = parent[pi]
                    size[pi] += size[pj]
                    
                
                else:
                    parent[pi] = parent[pj]
                    size[pj] += size[pi]
        
        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                val = abs(points[i][0] - points[j][0] ) + abs(points[i][1] - points[j][1])
                edges.append([val,i,j])
        

        edges.sort( key = lambda x:x[0])
        ans = 0

        for i , (x,y,z) in enumerate(edges):
            if find(y) != find(z):
                union(y,z)
                ans += x
        return ans
