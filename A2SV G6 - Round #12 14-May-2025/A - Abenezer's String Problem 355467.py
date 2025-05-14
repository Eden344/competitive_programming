# Problem: A - Abenezer's String Problem - https://codeforces.com/gym/606404/problem/A

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter,deque
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))
 
case = integer()
while case:
    case -= 1
    n = integer()
    word = string()
    word = word.lower()
    maxi = 0
    
    for char in word:
        if char.isalpha():
            val = ord(char) - ord('a') + 1
            if val > maxi:
                maxi = val
    
    print(maxi)