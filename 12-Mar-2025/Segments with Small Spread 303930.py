# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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


n,k = integers()
arr = List()
inc_que = deque() #stores max values
dec_que = deque() #stores min values
maxi = []
right = 0
for i in range(len(arr)):
            
    while inc_que and inc_que[-1] < arr[i]:
        inc_que.pop()
    inc_que.append(arr[i])

    while dec_que and dec_que[-1] >arr[i]:
        dec_que.pop()
    dec_que.append(arr[i])
    

    while inc_que[0] - dec_que[0] > k:
        num = arr[right]
        if dec_que[0] == num:
            dec_que.popleft()
        if inc_que[0] == num:
            inc_que.popleft()
        right += 1
    maxi.append(i - right + 1)
print(sum(maxi))
