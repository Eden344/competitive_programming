# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def my_pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            mid = my_pow(x,n//2)

            if n % 2 == 0:
                return mid * mid
            else:
                return x * mid * mid
        
        if n < 0:
            x = 1/x
            n = -n
        return my_pow(x,n)
       