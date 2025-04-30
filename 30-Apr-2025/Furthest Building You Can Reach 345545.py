# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, height: List[int], bricks: int, ladder: int) -> int:
        left = 0
        right = 1

        building = []

        while right < len(height):
            diff = height[right] - height[left]
            if diff <= 0:
                left += 1
                right += 1
            else:
                heapq.heappush(building, diff)
                if len(building) > ladder:
                    bricks -= heapq.heappop(building)

                if bricks < 0:
                    return left
                left += 1
                right += 1
        return len(height) - 1
            
            

            

        