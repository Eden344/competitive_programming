# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out =  [0 for _ in range(n)]
        chart = defaultdict(list)

        for i in range(n):
            for nbr in graph[i]:
                chart[nbr].append(i)
                out[i] += 1
        print (out)
        print(chart)

        que = deque()
        order = []

        for edge in range(n):
            if out[edge] == 0:
                que.append(edge)
        

        while que:
            last = que.popleft()
            order.append(last)
            for nbr in chart[last]:
                out[nbr] -= 1
                if out[nbr] == 0:
                    que.append(nbr)
        order.sort()
        
        return order

       
    
        
       



            

        