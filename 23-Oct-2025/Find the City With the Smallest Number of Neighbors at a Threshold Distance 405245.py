# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
      
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

       
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

       
        res_city = -1
        min_reach = float('inf')

        for i in range(n):
            reachable = sum(dist[i][j] <= distanceThreshold for j in range(n))
            
            
            if reachable < min_reach or (reachable == min_reach and i > res_city):
                min_reach = reachable
                res_city = i

        return res_city
