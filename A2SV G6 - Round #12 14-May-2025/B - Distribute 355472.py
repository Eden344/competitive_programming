# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

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
 
n = integer()
card = List()
idx_card = list(enumerate(card))
idx_card.sort(key = lambda x: x[1])
 
res = []
summ = idx_card[0][1] + idx_card[-1][1]
 
for i in range(n//2):
    left = idx_card[i]
    right = idx_card[n - 1 - i]
 
    if left[1] + right[1] != summ:
        pass
    res.append((left[0] + 1, right[0] + 1))
 
for num in res:
    print(*num)