# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        adjusted = [nums1[i] - nums2[i] for i in range(n)]
        
        sorted_list = SortedList()
        count = 0
        
        for j in range(n):
           
            target = adjusted[j] + diff
            
            count += sorted_list.bisect_right(target)
        
            sorted_list.add(adjusted[j])
        
        return count

