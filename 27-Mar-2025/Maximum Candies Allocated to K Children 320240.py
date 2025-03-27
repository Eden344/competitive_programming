# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        low = 0
        high = max(candies)

        def check(num):
            if num == 0:
                return True
            summ = 0
            for i in range (len(candies)):
                summ += candies[i]//num
            return summ >= k

        while low <= high:
            mid = (low + high)//2

            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1

        