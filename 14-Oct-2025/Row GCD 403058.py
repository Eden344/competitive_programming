# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

from functools import reduce
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

n,m = integers()

a = List()
b = List()

if n == 1:
    
    ans = [a[0] + bj for bj in b]
else:
    
    diffs = [a[i] - a[0] for i in range(1, n)]
    G = reduce(gcd, diffs)

   
    ans = [gcd(a[0] + bj, G) for bj in b]

print(*ans)