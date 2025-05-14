# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre_xor = [arr[0]]

        for i in range(1, n):
            pre_xor.append(pre_xor[i -1] ^ arr[i])
       

        ans = []
    

        for x, y in queries:
            if x != 0:
                res = pre_xor[y] ^ pre_xor[x - 1]
                ans.append(res)
            else:
                ans.append(pre_xor[y])
        return (ans)

        