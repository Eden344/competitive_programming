# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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


def max_prefix(arr):
    max_sum = 0
    curr_sum = 0
    
    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum


case = integer()
res = []
while case:
    case -=1
    n = integer()
    red = List()
    m = integer()
    blue = List()
    
    
    max_red = max_prefix(red)
    max_blue = max_prefix(blue)
    
    res.append(max(0,max_red + max_blue))
    
print("\n".join(map(str,res)))
    
    