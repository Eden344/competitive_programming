# Problem: A - Can I Get Your Number ? - https://codeforces.com/gym/607625/problem/A

import sys
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))
 
case = integer()
words = []
while case:
    case -= 1
    s = string()
    words.append(s)
 
if not words:
    print(0)
    sys.exit()
 
min_len = min(len(word) for word in words)
count = 0
 
for i in range(min_len):
    current_char = words[0][i]
    same = True
    for word in words:
        if word[i] != current_char:
            same = False
            break
    if same:
        count += 1
    else:
        break
 
print(count)