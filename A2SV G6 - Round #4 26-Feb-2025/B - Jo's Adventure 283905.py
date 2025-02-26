# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

num, query = integers()

arr = List()
arr = [0] + arr
ans = []
n = len(arr)
left = 0
right = left + 1
while right < n:
    if arr[left] > arr[right]:
        ans.append(arr[left] - arr[right])
        left += 1
        right += 1
    else:
        ans.append(0)
        left += 1
        right += 1
        
for i in range(1, len(ans)):
    ans[i] += ans[i - 1]


res =[]
nr = n -1
nl = nr - 1

while nl > 0:
    if arr[nr] < arr[nl]:
        res.append(0)
        nl -= 1
        nr -= 1
    else:
        res.append(arr[nr] - arr[nl])
        nl -= 1
        nr -= 1
res.append(0)
res = res[::-1]

for i in range(1, len(res)):
    res[i]+= res[i - 1]

   
    
        
        

        
        

while query:
    query -= 1
    l, r = integers()
    
    if r > l:
        diff = ans[r - 1] - ans[l -1]
    elif l == r:
        diff = 0
    else:
        diff = res[l-1] - res[r -1]
    print(diff)
    
    

