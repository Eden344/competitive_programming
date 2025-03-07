# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        my_dict = defaultdict(int)
        n = len(arr)
        target = n//2

        for num in arr:
            my_dict[num] += 1

        values = sorted(my_dict.values(), reverse = True)

        curr = 0
        count = 0

        for val in values:
            if curr >= target:
                break
            curr += val
            count += 1
        return count if curr >= target else -1



    

     

       



        



        