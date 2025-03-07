# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
     
        for char in tokens:
            if char in {"+", "-","*","/"}:
                prev = stk.pop()
                p_prev = stk.pop()
               

                if char == "+":
                    stk.append(p_prev + prev)
                elif char == "-":
                    stk.append(p_prev - prev)
                elif char == "*":
                    stk.append(p_prev *prev)
                elif char == "/":
                    stk.append(int(p_prev / prev))

            else:
                stk.append(int(char))

            
        return stk[0]


        