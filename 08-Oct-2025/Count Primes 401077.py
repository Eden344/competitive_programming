# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for _ in range(n + 1)]

        if n >= 0:
            prime[0] =  False
        if n >= 1:
            prime[0] = prime[1] = False

        i = 2
        while i * i <= n:
            if prime[i]:
                j = i * i
                while j <= n:
                    prime[j] = False
                    j += i
            i += 1
        cnt = 0
        for i in range(n):
            if prime[i] == True:
                cnt += 1
        return cnt
        