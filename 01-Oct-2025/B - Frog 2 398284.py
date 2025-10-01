# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import sys

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


n ,k = integers()
arr = List()

memo = {}
@bootstrap
def jump (start):

    if start == 0:
        yield 0
    if start == 1:
        memo[1] = abs(arr[start] - arr[0])
        yield memo[1]
    if start not in memo:
        
        mini = float('inf')

        for i in range(1, k + 1):
            if start - i >= 0:
                
                j1 = yield jump(start -i)

                mini = min(mini,abs(arr[start]- arr[start - i]) + j1)
        memo[start] = mini       
    yield memo[start]

print (jump(n - 1))

