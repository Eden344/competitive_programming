# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = 1  

        for i in range(len(pattern) + 1):
            stack.append(str(num))
            num += 1

            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return ''.join(result)
