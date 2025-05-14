# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

import sys
from collections import defaultdict
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))
 
def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        max_freq = max(freq.values())
        if max_freq <= n - max_freq:
            print(n % 2)
        else:
            print(max_freq - (n - max_freq))
 
if __name__ == "__main__":
    main()
