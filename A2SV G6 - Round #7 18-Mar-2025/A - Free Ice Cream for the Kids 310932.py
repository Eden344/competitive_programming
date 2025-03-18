# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

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

n, x = integers()
count = 0
stk = [x]
while n:

    n -= 1
    d = tuple(stringList())
    
    
    
    
    if d[0] == '+':
        x += int(d[1])
    else:
        if x < int(d[1]):
            count += 1
        else:
            x -= int(d[1])

   
print(x, count)
        
        
