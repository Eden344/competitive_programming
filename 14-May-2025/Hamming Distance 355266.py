# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x ^ y

        ans = []
        while val > 0:
            val1 = val % 2
            ans.append(val1)
            val = val // 2
      
        return ans.count(1)
        
