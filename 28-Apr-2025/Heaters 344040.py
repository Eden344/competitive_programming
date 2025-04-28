# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        
        for house in houses:
           
            idx = bisect_left(heaters, house)

            if idx > 0:
                left_heater = abs(house - heaters[idx -1])
            else:
                left_heater = float('inf')
            
            if idx < len(heaters):
                right_heater = abs(house - heaters[idx])
            else:
                right_heater = float('inf')

            
            radius = max(radius, min(left_heater, right_heater))

        return radius