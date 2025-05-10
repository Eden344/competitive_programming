# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def backtrack(start: int, path: List[str]):
            if len(path) == 4:  
                if start == len(s):  
                    result.append('.'.join(path))
                return
            
            for length in range(1, 4):  
                if start + length > len(s):  
                    break
                segment = s[start:start + length]
                
                if (length == 1 or (segment[0] != '0' and int(segment) <= 255)):
                    path.append(segment)  
                    backtrack(start + length, path)  
                    path.pop() 
        
        backtrack(0, [])
        return result

