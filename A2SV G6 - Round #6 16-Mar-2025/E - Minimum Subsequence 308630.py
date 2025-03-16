# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

import sys
from collections import deque

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())


t = integer()
for _ in range(t):
    n = integer()
    s = string()
    

    zero_stack = deque()
    one_stack = deque()
    res = []
    
    for i in range(n):
        if s[i] == '0':
            if one_stack:
                
                seq = one_stack.pop()
                zero_stack.append(seq)
            else:
                
                seq = len(zero_stack) + len(one_stack) + 1
                zero_stack.append(seq)
            res.append(seq)
        else:
            if zero_stack:
                
                seq = zero_stack.pop()
                one_stack.append(seq)
            else:
                
                seq = len(zero_stack) + len(one_stack) + 1
                one_stack.append(seq)
            res.append(seq)
    
    
    k = len(zero_stack) + len(one_stack)
    
    
    print(k)
    print(' '.join(map(str, res)))

