# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

import sys

def count_valid_segments(n, t, c, crimes):
    valid_count = 0
    count = 0
    
    for crime in crimes:
        if crime > t:
            count = 0  
        else:
            count += 1  
            if count >= c:
                valid_count += 1  
    
    return valid_count

def solve():
    input = sys.stdin.read
    data = input().split("\n")
    index = 0
    
    n, t, c = map(int, data[index].split())
    index += 1
    crimes = list(map(int, data[index].split()))
    
    print(count_valid_segments(n, t, c, crimes))
    
if __name__ == "__main__":
    solve()
