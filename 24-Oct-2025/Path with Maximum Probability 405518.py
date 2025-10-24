# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        for i , (u,v) in enumerate(edges):
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        
        heap = [(-1.0,start)]

        visit = set()

        while heap:
            curr_prob, node = heapq.heappop(heap)
            visit.add(node)

            if node == end:
                return curr_prob * -1
            for child, prob in graph[node]:
                if child not in visit:
                    heapq.heappush(heap,(curr_prob * prob, child))
        return 0


        

