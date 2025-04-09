# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:



        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    graph[i + 1].append(j + 1)
                    graph[j + 1] .append(i + 1)
        print(graph)

        visited = set()

        def dfs(node):
            visited.add(node)

            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr)

        
        count = 0

        for i in range(1, len(isConnected)+ 1):
            if i not in visited:
                dfs(i)
                count += 1
        return count








        
