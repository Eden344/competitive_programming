# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter,deque
from bisect import bisect_left, bisect_right
from itertools import accumulate
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))
 
ship, base = integers()
attack = List()
 
bases = [tuple(integers()) for _ in range(base)]
 
bases.sort(key= lambda x: x[0])
 
defense = [d for d, _ in bases]
 
gold = [g for _,g in bases]
pre_sum = list(accumulate(gold))
 
 
ans = []
 
for i in range(len(attack)):
    val = bisect_right(defense, attack[i])
    if val == 0:
        ans.append(0)
    else:
        ans.append(pre_sum[val - 1])
    
 
print(*ans)