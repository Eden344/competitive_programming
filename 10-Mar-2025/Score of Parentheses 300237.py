# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stk = [0]

        for char in s:
            if char == '(':
                stk.append(0)
            else:
                val = stk.pop()
                stk[-1] += max(2*val, 1)
        return stk[0]
               
        