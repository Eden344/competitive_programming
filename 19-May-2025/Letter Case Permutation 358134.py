# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        char = [i for i, ch in enumerate(s) if ch.isalpha()]
        n = len(char)
        res = []

        for bits in range(1 << n):
            chars = list(s)
            for j in range(n):
                idx = char[j]
                if (bits >> j) & 1:
                    chars[idx] = chars[idx].upper()
                else:
                    chars[idx] = chars[idx].lower()
            res.append("".join(chars))
        return res
