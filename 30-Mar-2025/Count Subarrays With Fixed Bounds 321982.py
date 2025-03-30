# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_pos = -1
        max_pos = -1
        left_bound = -1

        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = idx
            if num == minK:
                min_pos = idx
            if num == maxK:
                max_pos = idx
            count += max(0, min(min_pos, max_pos) - left_bound)

        return count