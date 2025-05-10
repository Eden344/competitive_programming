# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can(s: str, target: int, start: int) -> bool:
           
            if start == len(s):
                return target == 0
            
            curr = 0
            for i in range(start, len(s)):
                curr = curr * 10 + int(s[i])
                
                if curr > target:
                    break
                
                if can(s, target - curr, i + 1):
                    return True
            return False
        
        result = 0
        for i in range(1, n + 1):
            sqr = i * i
            
            if can(str(sqr), i, 0):
                result += sqr
                
        return result