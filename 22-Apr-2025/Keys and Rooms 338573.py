# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(node):
            visited.add(node)
            for room in rooms[node]:
                if room not in visited:
                    dfs(room)
        
        dfs(0)
        return (len(visited) == n)
