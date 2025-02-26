# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

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


case = integer()
while case:
    case -= 1
    arr = List()  
    max_num = max(arr)  
    max_count = arr.count(max_num)  
    
    res = []
    
    for i in range(len(arr)):
        if arr[i] == max_num and max_count == 1:
            res.append(0)  
        else:
            res.append(max_num - arr[i] + 1)  

    print(*res)
   
    