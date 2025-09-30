# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def steal (start):
           
            if start>=len(nums):
                return 0
    
            elif start not in memo:

                memo[start] = max(steal(start + 1), steal(start + 2) + nums[start])
            return memo[start]
        
        return steal(0)


       

        