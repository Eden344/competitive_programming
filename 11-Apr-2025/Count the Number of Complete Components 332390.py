# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0

        def dfs(node, nodes):
            visited.add(node)
            nodes.append(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr, nodes)

        for i in range(n):
            if i not in visited:
                nodes = []
                dfs(i, nodes)

                edge_count = 0
                for node in nodes:
                    edge_count += len(graph[node])
                edge_count //= 2  

                k = len(nodes)
                if edge_count == k * (k - 1) // 2:
                    count += 1

        return count
