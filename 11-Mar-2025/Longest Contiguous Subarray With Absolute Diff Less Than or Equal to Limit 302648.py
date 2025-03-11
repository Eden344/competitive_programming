# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_que = deque() #stores max values
        dec_que = deque() #stores min values
        maxi = 0
        right = 0
        for i in range(len(nums)):
            
            while inc_que and inc_que[-1] < nums[i]:
                inc_que.pop()
            inc_que.append(nums[i])

            while dec_que and dec_que[-1] >nums[i]:
                dec_que.pop()
            dec_que.append(nums[i])
            

            while inc_que[0] - dec_que[0] > limit:
                num = nums[right]
                if dec_que[0] == num:
                    dec_que.popleft()
                if inc_que[0] == num:
                    inc_que.popleft()
                right += 1
            maxi = max(maxi, i - right + 1)
        return maxi




        

        