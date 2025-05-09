# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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


n,m = integers()

parent = list(range(n + 1))
points = [0] * (n + 1)
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
            points[pj]-= points[pi]
           
        else:
            parent[pi] = parent[pj]
            size[pj] += size[pi]
            points[pi]-= points[pj]

def add(num):
    summ = 0
    while num != parent[num]:
        summ += points[num]
        num = parent[num]
    return summ + points[num]
ans = []
            
while m:
    m -= 1
    y = stringList()
   
          
    if y[0] == "join":
        union(int(y[1]),int(y[2]))
    elif y[0] == "add":
        idx = find(int(y[1]))
        val = int(y[2])
        points[idx] += val
    else:
        ans.append(add(int(y[1])))

for char in ans:
    print(char)
   



