# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F


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



input = sys.stdin.read
data = input().split()
n = int(data[0])
segments = []
index = 1
for _ in range(n):
    l = int(data[index])
    r = int(data[index + 1])
    segments.append((l, r))
    index += 2


events = []
for l, r in segments:
    events.append((l, 1))  
    events.append((r + 1, -1))  


events.sort()


curr = 0
prev = None
count = [0] * (n + 1)  
for pos, delta in events:
    if prev is not None and pos != prev:
        num = pos - prev
        if num > 0:
            count[curr] += num
    curr += delta
    prev = pos


print(" ".join(map(str, count[1:])))

