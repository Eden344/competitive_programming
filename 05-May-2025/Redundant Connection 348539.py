# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = {i: i for i in range(1, n+1)}
        size = [1 for _ in range(0, n+1)]

        def find(x):
            
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(i, j):
            pi = find(i)
            pj = find(j)

            if pi != pj:
                if size[pi-1] > size[pj-1]:
                    parent[pj] = parent[pi]
                    size[pi] += size[pj]
                else:
                    parent[pi] = parent[pj]
                    size[pj] += size[pi]

        res = []

        for u,v in edges:
            if find(u) == find(v):
                res.append([u,v])
            else:
                union(u,v)
        return res[-1]

        