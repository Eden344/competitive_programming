# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        
        for char in s:
            if char != ']':
                stk.append(char)
            else:
                word = ""
            
                while stk and stk[-1]  != '[':
                    word = stk.pop() + word
                stk.pop()
                num = ""

                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(int(num) * word)
        return "".join(stk)
        
        

        