# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        parent = {i: i for i in range(26)}
        size = [1 ] * 26

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi != pj:
                if size[pi] > size[pj]:
                    parent[pj] = pi
                    size[pi] += size[pj]
                else:
                    parent[pi] = pj
                    size[pj] += size[pi]

        for s in equations:
            if s[1:3] == "==":
                x = ord(s[0]) - ord('a')
                y = ord(s[3]) - ord('a')
                union(x,y)
        for s in equations:
            if s[1:3] == "!=":
                x = ord(s[0]) - ord('a')
                y = ord(s[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True




        