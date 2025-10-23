# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

n = int(input())
a = list(map(int, input().split()))

def reduce_number(x):
    while x % 2 == 0:
        x //= 2
    while x % 3 == 0:
        x //= 3
    return x

reduced = [reduce_number(x) for x in a]

if len(set(reduced)) == 1:
    print("Yes")
else:
    print("No")
