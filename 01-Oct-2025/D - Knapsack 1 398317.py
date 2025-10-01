# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

import sys
import itertools
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

n,k = integers()
w = [0] * n
v = [0] * n

for i in range(n):
    w[i],v[i] = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range( n -1, -1, -1):
    for cap in range(k + 1):
        exclude = dp[i + 1][cap]
        include = 0
        if cap >= w[i]:
            include = dp[i + 1] [cap - w[i]] + v[i]
        dp[i][cap] = max(include,exclude)
print( dp[0][k])