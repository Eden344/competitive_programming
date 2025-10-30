# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

import sys
import math
input = sys.stdin.readline

def can(s, d, a, k):
    total = 0
    for di, ai in zip(d, a):
        trips = (di + s - 1) // s  
        total += trips * ai
        if total > k:
            return False
    return True

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    lo, hi = 1, max(d)
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid, d, a, k):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)
