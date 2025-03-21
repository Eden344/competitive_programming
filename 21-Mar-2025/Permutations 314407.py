# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def back(store, arr):

            if not arr:
                ans.append(store[:])


            for i in range(len(arr)):
                back( store + [arr[i]], arr[:i] + arr[i + 1:])

        back([], nums)
        return ans


        