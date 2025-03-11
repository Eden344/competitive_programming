# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1
        while n > 0:
            num *= n
            n -= 1
        count = 0

        while num % 10 == 0 and num != 0:
            count += 1
            num//=10
        return count

        