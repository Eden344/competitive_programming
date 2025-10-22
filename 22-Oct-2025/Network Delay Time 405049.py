# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,x in times:
            graph[u].append( (v,x))
        
        
        def dijkstra(graph_n, start):
            distances = { node: float("inf") for node in range(1, n+1)}
            distances[start] = 0
            processed = set()

            heap = [(0,start)]
            while heap:
                curr_dis, curr_node = heapq.heappop(heap)

                if curr_node in processed:
                    continue
                processed.add(curr_node)


                for child, weight in graph_n[curr_node]:
                    dis = curr_dis + weight

                    if dis < distances[child]:
                        distances[child] = dis
                        heapq.heappush(heap,(dis,child))
            return distances
        res = dijkstra(graph,k)
       

        maxi = max(res.values())

        if maxi == float("inf"):
            return -1
        else:
            return maxi

        
           


        


    


    

      