# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n


        for start in range(n):
            if color[start] == -1:
                que = deque()
                que.append(start)
                color[start] = 0

            while que:
                node = que.popleft()
              
                for nbr in graph[node]:
                    if color[nbr] == -1:
                        color[nbr] = 1 - color[node]
                        que.append(nbr) 

                    elif color[nbr] == color[node]:
                        return False
        return True
                




            







        

        