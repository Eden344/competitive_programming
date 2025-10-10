# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())


div_count = [0] * (n + 1)


for i in range(2, n + 1):
    if div_count[i] == 0: 
        for j in range(i, n + 1, i):
            div_count[j] += 1


almost_primes = sum(1 for i in range(2, n + 1) if div_count[i] == 2)

print(almost_primes)
