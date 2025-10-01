# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import sys

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
n ,k = integers()
arr = List()
dp = [0] * n

dp[0] = 0


for i in range(1,n):
    mini = float("inf")
    for j in range(1, k + 1):
        if i - j >= 0:
            mini = min(mini, abs(arr[i] - arr[i - j] ) + dp[i - j])
    dp[i] = mini
print(dp[-1])