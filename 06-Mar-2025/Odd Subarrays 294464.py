# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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


case = integer()

while case:
    case -= 1
    num = integer()
    arr = List()
    count = 0
    right = 1
    
    while right < num:
        if arr[right - 1] > arr[right]:
            count += 1
            right += 1
        right += 1
    print(count)
    
   
    
    