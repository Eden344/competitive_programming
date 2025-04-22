# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        r_graph = defaultdict(list)
        for x,y in redEdges:
            r_graph[x].append(y)
        
        b_graph = defaultdict(list)
        for u,v in blueEdges:
            b_graph[u].append(v)
        

        ans = [float("inf")] * n

        def bfs(src,clr):
            que = deque()
            que.append((src,clr))
            visited = set()
            visited.add((src,clr))
            path = 0

            while que:
                n = len(que)

                for _ in range(n):
                    node,color = que.popleft()
                    ans[node] = min (ans[node],path)

                    if color == "blue":
                        for nbr in b_graph[node]:
                            if (nbr, "red") not in visited:
                                visited.add((nbr,"red"))
                                que.append((nbr,"red"))
                    else:
                        for nbr in r_graph[node]:
                            if (nbr, "blue") not in visited:
                                visited.add((nbr,"blue"))
                                que.append((nbr,"blue"))
                path += 1
        bfs(0,"blue")
        bfs(0,"red")

        for i in range(len(ans)):
            if ans[i] == float('inf'):
                ans[i] = -1

        return ans    


        


        

        

        