# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def possible(num):
            summ = 0
            count = 1
            for weight in weights:
                summ += weight

                if summ > num:
                    count += 1
                    summ = weight
            if count > days:
                return False
            return True

        high = sum(weights)
        low = max(weights)

        idx = 0

        while low <= high:
            mid = (low + high)//2
            if possible(mid):
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
        return idx
        
        

        