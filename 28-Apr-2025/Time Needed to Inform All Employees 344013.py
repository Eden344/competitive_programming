# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for employee in range(n):
            if manager[employee] != -1:
                graph[manager[employee]].append(employee)

        def dfs(employee: int) -> int:
            total_time = 0
            for sub in graph[employee]:
                total_time = max(total_time, dfs(sub))
            return total_time + informTime[employee]

        return dfs(headID)

