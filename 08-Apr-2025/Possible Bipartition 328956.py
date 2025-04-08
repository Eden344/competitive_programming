# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [-1] * (n + 1)
        ans = True


        def dfs(node, col):

            nonlocal ans

            mycolor = 1 - col
            color[node] = mycolor


            for nbr in graph[node]:
                if color[nbr] == -1:
                    dfs(nbr,mycolor)
                elif color[nbr] == mycolor:
                    ans = False
            # return ans


        for i in range (1, n + 1):
            if color[i] == -1:
                dfs(i, 0)
        return ans

