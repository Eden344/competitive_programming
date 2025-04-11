# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))


n, m = integers()
nodes = []

while m:
    m -= 1
    
    node, ver = integers()
    nodes.append([node,ver])
# print(nodes)

graph = defaultdict(list)

for u, v in nodes:
    graph[u].append(v)
    graph[v].append(u)
# print(graph)
# print(graph[1])

good = [0] * n

for i in range(n):
    good[i] = len(graph[i + 1])

one_cnt = 0
two_cnt = 0
for i in range(n):
    if good[i] == 1:
        one_cnt += 1
    elif good[i] == 2:
        two_cnt += 1
        

if one_cnt == 2 and two_cnt == n - 2:
    print("bus topology")
elif two_cnt == n:
    print("ring topology")
elif one_cnt == n -1 and max(good) == n - 1:
    print("star topology")
else:
    print("unknown topology")


        
            
    
    
        
    


    
    