# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = []
        res = []

        for i, num in enumerate(temp):
            if num > stk[i][1]:
                stk.pop()
                ans.append(i - stk[0][0])
            else:
                stk.append([i,num])
        return ans
        