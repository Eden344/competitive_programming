# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        F = [0,1,1]
        for i in range (3, n + 1):
            F.append(F[i -1] + F[i - 2] + F[i -3])
        return F[n]

            
       

