# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stks = []
        stkt = []

        for char in s:
            if char =="#":
                if stks:
                    stks.pop()
            else:
                stks.append(char)
        print(stks)
        
        for cha in t:
            if cha == "#":
                if stkt:
                    stkt.pop()
            else:
                stkt.append(cha)
        print(stkt)

        if stks == stkt:
            return True
        else:
            return False
        