# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.rank[pa] += self.rank[pb]


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        edgeList.sort(key=lambda x: x[2])
        
        queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        queries.sort(key=lambda x: x[2])  
       
        dsu = DSU(n)
        res = [False] * len(queries)
        i = 0  
        
        for p, q, limit, idx in queries:
           
            while i < len(edgeList) and edgeList[i][2] < limit:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            
           
            if dsu.find(p) == dsu.find(q):
                res[idx] = True
        
        return res
