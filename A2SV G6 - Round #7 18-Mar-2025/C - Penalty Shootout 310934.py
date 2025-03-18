# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

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

case = integer()

while case:
    case -= 1
    pen = list(map(str,string()))
    
    idx1 = 0
    idx2 = 0
    team1 = 0
    team2 = 0
    
    rem1 = 5
    rem2 = 5
    
    for i in range(len(pen)):
        if i % 2 == 0:
            if pen[i] == '1' or pen[i] == '?':
                team1 += 1
            rem1 -= 1
        else:
            if pen[i] =='1':
                team2 += 1
            rem2 -= 1
        if team1 > team2 + rem2:
            idx1 =i + 1
            break
    else:
        idx1 = 10
        
    team1 = 0
    team2 = 0
    
    rem1 = 5
    rem2 = 5
    
    for i in range(len(pen)):
        if i % 2 == 0:
            if pen[i] == '1' :
                team1 += 1
            rem1 -= 1
        else:
            if pen[i] =='1' or pen[i] == '?':
                team2 += 1
            rem2 -= 1
        if team2 > team1 + rem1:
            idx2 = i + 1
            break
    else:
        idx2 = 10
    
    
    print(min(idx1,idx2))
    
    
    
    