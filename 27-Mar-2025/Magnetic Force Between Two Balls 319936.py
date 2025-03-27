# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        def check(num):
            count = 1
            last = pos[0]
            for i in range(1,len(pos)):
                if pos[i] - last >= num:
                    count += 1
                    last = pos[i]
                if count == m:
                    return True
            return False



        
        low = 1
        high = pos[-1] - pos[0]

        while low <= high:
            mid = (low + high)//2

            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
            
        return high




        

        