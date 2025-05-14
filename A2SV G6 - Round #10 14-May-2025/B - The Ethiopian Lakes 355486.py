# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

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
from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
 
case = integer()
 
while case:
    case -= 1
    
    n,m = integers()
    
    mat = Matrix(n)
    
    # print(mat)
    
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    
    visited = set()
    
    # print(visited)
    def inbound(row,col):
            return (0 <= row < n and 0 <= col < m)
   
    @ bootstrap
    def dfs(row,col):
        
        if not inbound(row, col) or (row,col) in visited or mat[row][col] == 0:
            yield 0
        else:
            ans = mat[row][col]
        visited.add((row,col)) 
       
        
        for x,y in moves:
            n_row = row + x
            n_col = col + y
            if inbound(n_row,n_col)  and  mat[n_row][n_col] != 0:
                ans += yield dfs(n_row,n_col)
        # print(ans)
        yield ans
    
    maxi = 0
            
    for i in range(n):
        for j in range(m):
            if mat[i][j] != 0:
                maxi = max(maxi, dfs(i,j))
    print(maxi)