# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = Counter([a % k for a in arr])
        for r in range(k):
            if r == 0:
                if rem[r] % 2 != 0:
                    return False
            else :
                if rem[r] != rem[k - r]:
                    return False
        return True

        