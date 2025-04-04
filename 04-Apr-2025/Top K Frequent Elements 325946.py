# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        sorted_keys = sorted(my_dict.keys(), key=lambda key: my_dict[key], reverse=True)
        
        
        return sorted_keys[:k]