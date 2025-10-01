# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for a in arr:
            if a - difference in dp:
                dp[a] = 1 + dp[a - difference]
            else:
                dp[a] = 1
        return max(dp.values())
