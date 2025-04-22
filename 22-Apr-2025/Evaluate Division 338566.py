# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, e: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            u , v = e[i][0], e[i][1]
            graph[u].append((v,values[i]))
            graph[v].append((u,1/values[i]))

        visited = set()

        def dfs(node):
            visited.add(node)
            if node == destination:
                return 1

            for x, y in graph[node]:
                if x not in visited:
                    ret = dfs(x)
                    if ret != -1:
                        return ret*y
            return -1

        ans = []
        for source , desti in queries:
            if source not in graph or desti not in graph:
                ans.append(-1)
                continue
            visited = set()
            destination = desti
            ans.append(dfs(source))

        return ans
