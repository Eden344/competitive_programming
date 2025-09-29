# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last = stones[-1]
        stones_set = set(stones)

        @lru_cache(None)
        def dp( i,k):
            if i == last:
                return True

            for j in range(k - 1, k + 2):
                if j > 0 and (j + i )in stones_set:
                    if dp (i + j, j):
                        return True
            return False

            
                
        return dp(0,0)