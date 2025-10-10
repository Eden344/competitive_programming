# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        def gcd(a,b):
            if b == 0:
                return a
            
            return gcd(b, a%b)
        return gcd(maxi,mini)    