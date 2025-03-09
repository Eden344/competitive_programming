# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

import sys

def solve():
    input = sys.stdin.read
    data = input().split("\n")
    index = 0
    q = int(data[index])
    index += 1
    results = []
    
    for _ in range(q):
        if data[index] == "":
            index += 1  
        
        n, k = map(int, data[index].split())
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        t = list(map(int, data[index].split()))
        index += 1
        
        
        inf = float('inf')
        temperatures = [inf] * n
        
        
        for i in range(k):
            temperatures[a[i] - 1] = t[i]
        
        
        for i in range(1, n):
            temperatures[i] = min(temperatures[i], temperatures[i-1] + 1)
        
        
        for i in range(n-2, -1, -1):
            temperatures[i] = min(temperatures[i], temperatures[i+1] + 1)
        
        results.append(" ".join(map(str, temperatures)))
    
    print("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
