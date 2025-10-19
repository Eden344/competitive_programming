# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from math import sqrt
from collections import Counter

def factorize(x):
    factors = Counter()
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors[d] += 1
            x //= d
        d += 1
    if x > 1:
        factors[x] += 1
    return factors

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = Counter()
    for num in a:
        total += factorize(num)
    
    possible = all(exp % n == 0 for exp in total.values())
    print("YES" if possible else "NO")
