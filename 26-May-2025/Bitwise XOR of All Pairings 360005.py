# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = reduce(xor, nums1)
        xor2 = reduce(xor, nums2)
        
        num1 = (len(nums1) % 2) * xor2
        num2 = (len(nums2) % 2) * xor1

        return num1 ^ num2
        