# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canMakeZero(k: int) -> bool:
            n = len(nums)
            
            diff = [0] * (n + 1)
            
            
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            
            
            less = [0] * n
            curr = 0
            for i in range(n):
                curr += diff[i]
                less[i] = curr

            
            for i in range(n):
                if nums[i] > less[i]:
                    return False
            return True

       
        low, high = 0, len(queries)
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if canMakeZero(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
