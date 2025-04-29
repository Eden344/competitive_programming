# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        while nums[0] < k:
            num1 = heapq.heappop(nums)
            num2 = heapq.heappop(nums)
            val = min(num1,num2) * 2 + (max(num1,num2))
            heapq.heappush(nums,val)
            ans += 1
        return ans
        
