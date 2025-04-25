# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = [i for i in range(n)]
        graph = defaultdict(list)
        outside = [0 for _ in range(n)]

        for u,v in richer:
            graph[u].append(v)
            outside[v] += 1
        
        # print(inside)

        que  = deque()
        

        for i in range(n):
            if outside[i] == 0:
                que.append(i)
        

        print(outside)
        # print(que)
        # print(graph)
        while que:

            node = que.popleft()
            
            for nbr in graph[node]:
                outside[nbr] -= 1
                # print(node, nbr)
                num1 = ans[node]
                num2 = ans[nbr]
                if quiet[num1] < quiet[num2]:
                    ans[nbr] = num1
                if outside[nbr] == 0:
                    que.append(nbr)
                    

        return ans
