# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

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


n, k = integers()

arr = List()
que = deque()
hash = defaultdict(int)
for i in range(len(arr)):
    if hash[arr[i]] != 0:
        continue  
    
    if len(que) == k:
        idx = que.pop()
        hash[idx] -= 1
    que.appendleft(arr[i])
    hash[arr[i]] += 1
            

        
        
print(len(que))
print(*que)
        