# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_cnt = s.count('1')
        arr = [0] * len(s)

       
        if one_cnt == 1:
            arr[-1] = 1
        if one_cnt > 1:
            arr[-1] = 1
            for i in range(one_cnt -1):
                arr[i] = 1
        return ''.join(map(str, arr))

        