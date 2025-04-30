# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        grid_sort = [sorted(row, reverse=True)[:limits[i]] for i, row in enumerate(grid)]
        arr = []
        for i in range(len(grid_sort)):
            for j in range(len(grid_sort[i])):
                arr.append(grid_sort[i][j])
   
        for i in range(len(arr)):
            num = -1 * arr[i]
            arr[i] = num
      
        heapq.heapify(arr)
        arr2 = []
        while k > 0:
            k -= 1
            num = heapq.heappop(arr)
            arr2.append(num)
       

        return abs(sum(arr2))
      

        




        