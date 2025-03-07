# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stk:
                    stk.pop()
            elif part =="." or part =='':
                continue
            else:
                stk.append(part)
        return "/" + '/'.join(stk)

        




