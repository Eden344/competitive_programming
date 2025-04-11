# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
        # print(graph)
       

        def dfs(node, visited):
           

            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr, visited)

        
        for i in range(n):
            visited = set()
            dfs(i, visited)
            if len(visited) == n -1 :
                return i
        return -1


