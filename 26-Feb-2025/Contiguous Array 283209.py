# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {0: -1}  
        count = 0  
        max_length = 0  
        
        for i in range(len(nums)):
            
            count += 1 if nums[i] == 1 else -1
            
            if count in count_map:
               
                max_length = max(max_length, i - count_map[count])
            else:
                
                count_map[count] = i
        
        return max_length

