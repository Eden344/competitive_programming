# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        stk = []
        res = [0] * n

        for i, num in enumerate(temp):
            while stk and temp[stk[-1]] < num:
                prev = stk.pop()
                res[prev] = i - prev
            stk.append(i)

        return res
                
            
        