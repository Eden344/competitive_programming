# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stk = []
        for char in logs:
            if char =="../":
                if stk:
                    stk.pop()
            elif char =="./":
                pass
            else:
                stk.append(char)
        return len(stk)

       

        
        