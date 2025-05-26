# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi != pj:
                if size[pi] < size[pj]:
                    pi, pj = pj, pi  
                parent[pj] = pi
                size[pi] += size[pj]

        def same(w1, w2):
            if w1 == w2:
                return True
            diffs = [(a, b) for a, b in zip(w1, w2) if a != b]
            return len(diffs) == 2 and diffs[0] == diffs[1][::-1]

        for i in range(n):
            for j in range(i + 1, n):
                if same(strs[i], strs[j]):
                    union(i, j)

        roots = set(find(i) for i in range(n))
        return len(roots)
