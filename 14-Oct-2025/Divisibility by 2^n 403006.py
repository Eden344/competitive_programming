# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys
import math
from math import ceil, gcd, log2,prod
from collections import defaultdict, Counter, deque

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

def cnt_two(x):
    cnt = 0
    while x % 2 == 0:
        x//= 2
        cnt += 1
    return cnt


case = integer()
while case:
    case -= 1
    n = integer()
    arr = List()
    total_twos = sum(cnt_two(a) for a in arr)

    if total_twos >= n:
        print(0)
        continue
    idx_twos = [cnt_two(i) for i in range(1, n + 1)]
    idx_twos.sort(reverse=True)

    ops = 0

    for twos in idx_twos:
        total_twos += twos
        ops += 1
        if total_twos >= n:
            break
    print(ops if total_twos >= n else -1)