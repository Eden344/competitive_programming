# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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

n,m,k = integers()
parent = list(range(n + 1))
points = [0] * (n + 1)
size = [1] * (n + 1)
comp = defaultdict(set)

def find(x):                                                            
    
    if x != parent[x]:
        parent[x] = find(parent[x])
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
            


            
q = []

for i in range(n):
    x,y = integers()

for i in range(k):
    q.append(stringList())
q= q[::-1]
ans = []

for i in range(k):
    
        if q[i][0] == "ask":
            if find(int(q[i][1])) == find(int(q[i][2])):
                ans.append("YES")
            else:
                ans.append("NO")
        elif q[i][0] == "cut":
            union(int(q[i][1]),int(q[i][2]))

ans= ans[::-1]
for char in ans:
    print(char)











    