# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque

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

    check = False
    count = 0
    ans = 0

    for i in range(32):
        if n &(1 << i):
            if not check:
                ans += 2 ** i
                check = True
            count += 1
    
    if count == 1:
        if ans == 1:
            ans += 2
        else:
            ans += 1
    print(ans)
