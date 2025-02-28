# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ps = [0] * len(nums)
        for i in range (1, len(nums)):
            nums[i] += nums[i - 1]
        nums.sort()
       
        summ = 0

        if all(x < 0 for x in nums):
            summ = abs(nums[0])
        elif all(x > 0 for x in nums):
            summ = nums[-1]
        else:
            summ = nums[-1] + abs(nums[0])
        return summ
           

        