# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

import sys

def integer(): return int(sys.stdin.readline().strip())
def List(): return list(map(int, sys.stdin.readline().strip().split()))


n = integer()
a = List()
m = integer()
b = List()


if sum(a) != sum(b):
    print(-1)
else:
    i, j = 0, 0
    sum1, sum2 = 0, 0
    count = 0

    while i < n and j < m:
        sum1 += a[i]
        sum2 += b[j]

        i += 1
        j += 1

        while sum1 != sum2:
            if sum1 < sum2 and i < n:
                sum1 += a[i]
                i += 1
            elif sum2 < sum1 and j < m:
                sum2 += b[j]
                j += 1
            else:
                break

        if sum1 == sum2:
            count += 1
            sum1 = sum2 = 0  

    print(count)
