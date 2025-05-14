# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

import sys
from collections import defaultdict
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))
 
 
 
n = integer()
p = List()
 
parent = [i for i in range(n + 1)]  
 
def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u
 
def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_v] = root_u
 
for i in range(1, n + 1):
    union(i, p[i - 1])
 
roots = set()
for i in range(1, n + 1):
    roots.add(find(i))
 
print(len(roots))