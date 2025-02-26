# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

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
    length, query = integers()
    arr = List()
    
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    arr = [0] + arr
    
    while query:
        query -= 1
        l, r, k = integers()
       
            
        diff = arr[r] - arr[l - 1]
        
        window = r - l +1
        
        ans = (arr[-1] - diff) + (window * k)
        
        if ans % 2 == 0:
            print("NO")
        else:
            print("YES")
        
        
        
        
        
    