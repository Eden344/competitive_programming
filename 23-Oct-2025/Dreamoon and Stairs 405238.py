# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

import math

n, m = map(int, input().split())

min_moves = math.ceil(n / 2)

for moves in range(min_moves, n + 1):
    if moves % m == 0:
        print(moves)
        break
else:
    print(-1)
