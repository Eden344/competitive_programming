# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp (i):
            if i >= len(questions):
                return 0
            if i in memo:
                return memo[i]

            skip = dp (i + 1)

            points, brainpower = questions[i]
            take  = points + dp( i + brainpower + 1)

            memo[i] = max(skip,take)
            return memo[i]

        
        return dp(0)

        