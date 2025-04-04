# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_set = set()
        n = len(nums)

        for num in nums:
            my_set.add(num)
        for val in range(len(nums) + 1):
            if val not in nums:
                return val
        