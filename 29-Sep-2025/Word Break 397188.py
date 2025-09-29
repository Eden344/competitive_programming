# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        @lru_cache(None)

        def dp(i):
            if i == len(s):
                return True
            
            for j in range( i + 1, len(s) + 1):
                if s[i:j] in wordDict and dp(j):
                    return True
            return False

        return dp(0)