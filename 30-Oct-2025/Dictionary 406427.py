# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

t = int(input())
for _ in range(t):
    s = input().strip()
    x, y = s[0], s[1]
    
    index = (ord(x) - ord('a')) * 25
    add = ord(y) - ord('a')
    
    if y > x:
        add -= 1
        
    print(index + add + 1)
