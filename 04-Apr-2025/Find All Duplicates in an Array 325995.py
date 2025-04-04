# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            right_pos = nums[i] - 1
            if nums[i] != nums[right_pos]:
                nums[i], nums[right_pos] = nums[right_pos], nums[i]
            else:
                i += 1

        ans = []

        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans
