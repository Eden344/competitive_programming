# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            right_pos = nums[i] - 1
            if nums[i] != nums[right_pos]:
                nums[i], nums[right_pos] = nums[right_pos], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return  []

