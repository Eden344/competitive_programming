# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = {chr(i):chr(i) for i in range(ord('a'), ord('z') + 1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            elif px < py:
                parent[py] = px
            else: 
                parent[px] = py
        
        for a,b in zip(s1,s2):
            union(a,b)
        
        return "".join(find(ch) for ch in baseStr)
       

        
        

       

        
        