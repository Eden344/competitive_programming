# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
edges = []


parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    
    if parent[x] != x:
        return find(parent[x])
    return parent[x]


def union(i, j):
    
    pi = find(i)
    pj = find(j)

    if pi != pj:
        if size[pi] > size[pj]:
            parent[pj] = parent[pi]
            size[pi] += size[pj]
            
           
        else:
            parent[pi] = parent[pj]
            size[pj] += size[pi]
            

while m:
    m -= 1
    edg1, edg2, w = integers()
    edges.append([w,edg1,edg2])



edges.sort(key = lambda x :x[0])

ans = 0
for i, (x, y, z) in enumerate(edges):
    if find(y) != find(z):
        union(y,z)
        ans += x

print(ans)

