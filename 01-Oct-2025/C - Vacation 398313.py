# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

import sys

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

n = integer()
a = [0] * n
b = [0] * n
c = [0] * n

for i in range (n):
    a[i],b[i],c[i] = map(int, input().split())

prevA, prevB,prevC = a[0],b[0],c[0]
for i in range(1,n):
    currA = a[i] + max(prevB,prevC)
    currB = b[i] + max(prevA,prevC)
    currC = c[i] + max(prevA,prevB)
    prevA,prevB,prevC = currA,currB,currC

print (max(prevA,prevB,prevC))

