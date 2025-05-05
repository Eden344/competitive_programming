# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
       
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        
       
        while n > 2:
            size = len(leaves)
            n -= size  
            for _ in range(size):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)  
                    if len(graph[neighbor]) == 1:  
                        leaves.append(neighbor)
        
        return list(leaves)  
        