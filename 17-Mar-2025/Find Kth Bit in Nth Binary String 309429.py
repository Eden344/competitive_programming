# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"  
        
        length = (1 << n) - 1  
        mid = length // 2 + 1   

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
           
            idx = length - k + 1
            return "0" if self.findKthBit(n - 1, idx) == "1" else "1"
