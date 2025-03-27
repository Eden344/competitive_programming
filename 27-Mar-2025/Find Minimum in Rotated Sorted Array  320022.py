# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mini = nums[0]

        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= mini:
                low = mid + 1
            else:
                mini = nums[mid]
                high = mid - 1
        return mini
     