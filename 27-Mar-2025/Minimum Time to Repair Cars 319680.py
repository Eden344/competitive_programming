# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(num):
            nonlocal cars
            car = 0
            for n in ranks:
                car += int(math.sqrt(num//n))
                
            return car >= cars





        low = 1
        high = min(ranks) * (cars * cars)


        while low < high:
            mid = (low + high)//2

            if check(mid):
                high = mid

            else:
                low = mid + 1
        return low
        

