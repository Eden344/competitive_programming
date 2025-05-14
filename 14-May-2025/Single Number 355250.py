# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        summ = 0
        for num in nums:
            summ ^= num
        return summ
        