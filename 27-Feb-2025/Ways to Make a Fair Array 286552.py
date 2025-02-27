# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_sum_r, even_sum_r = 0,0
        odd_sum_l, even_sum_l = 0,0
        summ = []
        ans = 0
        
        for i in range(len(nums)-1, -1, -1):
            summ.append([odd_sum_r, even_sum_r, odd_sum_l, even_sum_l])
            if i%2:
                odd_sum_r += nums[i]
            else:
                even_sum_r += nums[i]
        
        summ = summ[::-1]
        for i in range(len(nums)):
            summ[i][2], summ[i][3] = odd_sum_l, even_sum_l
            if i%2:
                odd_sum_l += nums[i]
            else:
                even_sum_l += nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            if summ[i][2] + summ[i][1] == summ[i][3] + summ[i][0]:
                ans += 1
                
        return ans