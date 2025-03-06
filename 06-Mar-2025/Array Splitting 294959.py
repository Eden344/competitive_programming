# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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


n, k = integers()
arr = List()
last = k - 1
res = []
for i in range(1, len(arr)):
    res.append(arr[i] - arr[i - 1])


res.sort()
summ = 0
for i in range(n - k):
    summ += res[i]
    
print(summ)
