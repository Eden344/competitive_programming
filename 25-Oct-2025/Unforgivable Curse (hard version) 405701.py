# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

import sys
import math
from collections import defaultdict

input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.rank[xr] += self.rank[yr]

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input().strip()
    t = input().strip()

    dsu = DSU(n)

    for i in range(n):
        if i + k < n:
            dsu.union(i, i + k)
        if i + k + 1 < n:
            dsu.union(i, i + k + 1)

    group_s = defaultdict(list)
    group_t = defaultdict(list)

    for i in range(n):
        root = dsu.find(i)
        group_s[root].append(s[i])
        group_t[root].append(t[i])

    possible = True
    for key in group_s:
        if sorted(group_s[key]) != sorted(group_t[key]):
            possible = False
            break

    print("YES" if possible else "NO")
