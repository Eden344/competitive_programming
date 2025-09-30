# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp ( i, total):
            if i == n:
                if total == target:
                    return 1
                else:
                    return 0
            if ( i, total) in memo:
                return memo[(i,total)]
            
            memo[(i,total)] = dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])
            return dp ( i, total)
        return dp(0,0)

            
        