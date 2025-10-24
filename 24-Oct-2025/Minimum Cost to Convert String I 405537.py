# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(len(cost)):
            graph[original[i]].append((changed[i],cost[i]))

        def dijkstra(strt):
            heap = [(0,strt)]
            min_cost = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost:
                    continue
                min_cost[node] = cost

                for nbr,nbr_cost in graph[node]:
                    heapq.heappush(heap,(cost + nbr_cost, nbr))
            return min_cost
             
        

        
        

        ans = {c:dijkstra(c) for c in set(source)}

        res = 0

        for x,y in zip(source,target):
            if y not in ans[x]:
                return -1
            res += ans[x][y]
        return res
            
        




            

