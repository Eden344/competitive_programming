# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        char_to_indices = defaultdict(list)
        for i, c in enumerate(ring):
            char_to_indices[c].append(i)
        
        @lru_cache(None)
        def dfs(ring_index, key_index):
            if key_index == len(key):
                return 0
            target_char = key[key_index]
            min_steps = float('inf')
            for next_index in char_to_indices[target_char]:
                # distance in circular ring
                diff = abs(next_index - ring_index)
                step = min(diff, n - diff) + 1  # +1 for pressing
                min_steps = min(min_steps, step + dfs(next_index, key_index + 1))
            return min_steps
        
        return dfs(0, 0)
        