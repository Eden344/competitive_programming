# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stk = []
        n = len(arr)
        left = [0] * n
        right = [0] * n

        
        for i in range(n):
            count = 1
            while stk and stk[-1][0] > arr[i]:
                count += stk.pop()[1]
            stk.append((arr[i], count))
            left[i] = count

        stk = []

        
        for i in range(n - 1, -1, -1):
            count = 1
            while stk and stk[-1][0] >= arr[i]:  
                count += stk.pop()[1]
            stk.append((arr[i], count))
            right[i] = count

       
        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD

        return result
