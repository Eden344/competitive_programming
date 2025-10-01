# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import sys

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
n = integer()
arr = List()
dp = [0] * n

dp[0] = 0
dp[1] = abs(arr[1] - arr[0])

for i in range(2,n):
    dp[i] = min(abs(arr[i] - arr[i - 1]) + dp[i - 1], abs(arr[i] - arr[i - 2]) + dp[i - 2])
print (dp[-1])