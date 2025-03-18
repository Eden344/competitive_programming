# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)

        ans = [0] * n
        
        for i in range(n-1,-1,-1):
            ans[i] = nums[i]
            
            for j in range(i+1, n):
                ans[j] = max(nums[i]-ans[j],
                             nums[j]-ans[j-1])
            
        return ans[n-1] >= 0