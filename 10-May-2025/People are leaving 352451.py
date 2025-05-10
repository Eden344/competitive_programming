# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
from collections import deque

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

n, m = integers()

parent = list(range(n + 2)) 

def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while x != root:
        next_x = parent[x]
        parent[x] = root
        x = next_x
    return root

output = []

for _ in range(m):
    q = string()
    if q[0] == '-':
        _, x = q.split()
        x = int(x)
        parent[x] = x + 1  
    else:
        _, x = q.split()
        x = int(x)
        res = find(x)
        if res > n:
            output.append("-1")
        else:
            output.append(str(res))

print("\n".join(output))
