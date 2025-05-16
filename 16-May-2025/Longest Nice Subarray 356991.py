# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxi = 0
        curr = 0
        left = 0
        for right in range(len(nums)):
            while( curr & nums[right]) != 0:
                curr ^= nums[left]
                left += 1
            curr |= nums[right]
            maxi = max(maxi, right - left + 1)
        return maxi

        