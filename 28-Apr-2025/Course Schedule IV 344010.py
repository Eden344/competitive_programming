# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, num: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
       
        graph = defaultdict(list)
        for a, b in pre:
            graph[a].append(b)

        
        def dfs(course, visited):
            if course in visited:
                return visited[course]
            
            able = set()
            for neighbor in graph[course]:
                able.add(neighbor)
                able.update(dfs(neighbor, visited))
            visited[course] = able
            return able

        
        visited = {}
        for course in range(num):
            if course not in visited:
                dfs(course, visited)

      
        result = []
        for u, v in queries:
            result.append(v in visited.get(u, set()))

        return result
        