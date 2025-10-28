# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        que = deque([1])
        curr_time = 0
        res = -1
        visited = defaultdict(list)

        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node == n:
                    if res != -1:
                        return curr_time
                    res = curr_time
                for child in graph[node]:
                    child_time = visited[child]
                    if len(child_time) == 0 or (len(child_time) == 1 and child_time[0] != curr_time):
                        que.append(child)
                        child_time.append(curr_time)
            if (curr_time// change) % 2 == 1:
                curr_time += change - (curr_time % change)
            
            curr_time += time

    

     
        