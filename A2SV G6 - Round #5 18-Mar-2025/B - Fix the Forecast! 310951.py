# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    na = list(enumerate(a))
    b.sort()
    na.sort(key = lambda x: x[1])


    

    ans = [0] * n
    for i in range(n):
       ans [na[i][0]] = b[i]


    return ans




t = int(input())
for _ in range(t):
    ans = solve()
    print(*ans)