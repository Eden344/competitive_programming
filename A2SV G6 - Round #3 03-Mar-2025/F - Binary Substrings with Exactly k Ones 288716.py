# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

import sys
from collections import defaultdict

k=int(input())
list1=list(map(int,input().strip()))
count=defaultdict(int)
count[0]=1
summ=0
res=0
for num in list1:
    summ+=num
    if summ-k in count:
        res+=count[summ-k]
    count[summ]+=1
print(res)


