# Problem: A - Two Ranges - https://codeforces.com/gym/604781/problem/A

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
    arr = List()
    arr2 = [arr[0]]
    for i in range(2, len(arr)):
        if arr[i] != arr2[0]:
            arr2.append(arr[i])
            break
    print(*arr2)