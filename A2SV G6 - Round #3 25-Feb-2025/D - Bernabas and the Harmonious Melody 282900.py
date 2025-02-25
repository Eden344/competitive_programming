# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))




t = integer() 
results = []

for _ in range(t):
    n = integer()  
    s = string()
    
   
    if s == s[::-1]:
        results.append("0")
        continue
    
    unique_chars = set(s)  
    min_removals = float('inf')

    for skip_char in unique_chars:
        left, right = 0, n - 1
        removals = 0
        possible = True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] == skip_char:
                left += 1
                removals += 1
            elif s[right] == skip_char:
                right -= 1
                removals += 1
            else:
                possible = False
                break

        if possible:
            min_removals = min(min_removals, removals)

    results.append(str(min_removals) if min_removals != float('inf') else "-1")


print("\n".join(results) + "\n")
