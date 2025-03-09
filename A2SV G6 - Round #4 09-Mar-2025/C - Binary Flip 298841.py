# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

import sys

def solve():
    input = sys.stdin.read
    data = input().split("\n")
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = data[index]
        index += 1
        b = data[index]
        index += 1
        
        
        if a == b:
            results.append("YES")
            continue
        
        
        zero_count = [0] * (n + 1)
        one_count = [0] * (n + 1)
        
        for i in range(n):
            zero_count[i + 1] = zero_count[i] + (a[i] == '0')
            one_count[i + 1] = one_count[i] + (a[i] == '1')
        
       
        flip = False
        possible = True
        
        for i in range(n - 1, -1, -1):
            if (a[i] == b[i]) == flip:  
                if zero_count[i + 1] != one_count[i + 1]:  
                    possible = False
                    break
                flip = not flip 
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
