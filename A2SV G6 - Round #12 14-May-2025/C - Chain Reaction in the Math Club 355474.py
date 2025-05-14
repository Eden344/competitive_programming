# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

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
 
 
 
n, m = integers()
 
adj = [set() for _ in range(n+1)]
 
for _ in range(m):
    a, b = integers()
    adj[a].add(b)
    adj[b].add(a)
 
groups = 0
 
while True:
    q = deque()
    
    for i in range(1, n+1):
        if len(adj[i]) == 1:
            q.append(i)
 
    if not q:
        break
 
    groups += 1
 
    while q:
        student = q.popleft()
        if adj[student]:  
            neighbor = adj[student].pop()
            adj[neighbor].remove(student)
 
print(groups)