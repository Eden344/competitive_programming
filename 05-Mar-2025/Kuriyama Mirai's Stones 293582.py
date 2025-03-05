# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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

num = integer()
cost = List()
sorted_cost = sorted(cost)



for i in range(1,len(cost)):
    cost[i] += cost[i - 1]


for j in range(1, len(sorted_cost)):
    sorted_cost[j] += sorted_cost[j - 1]


    
    



query = integer()
ans = 0

while query:
    query -= 1
    t,l,r = integers()
    
    if t == 1:
        if l == 1:
            ans = cost[r -1]
        else:
            ans = cost[r - 1] - cost[l - 2]
        
        
    else:
        if l == 1:
            ans = sorted_cost[r -1]
        else:
            ans = sorted_cost[r - 1] - sorted_cost[l - 2]
    print(ans)
        
    