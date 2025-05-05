# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
       
        idx_task = [(entime, protime, index) for index, (entime, protime) in enumerate(tasks)]
       
        idx_task.sort()
        result = []
        min_heap = []
        time = 0
        i = 0  
        
        while i < len(idx_task) or min_heap:
           
            while i < len(idx_task) and idx_task[i][0] <= time:
                entime, protime, index = idx_task[i]
                heapq.heappush(min_heap, (protime, index))
                i += 1
            
            if min_heap:
                protime, index = heapq.heappop(min_heap)
                result.append(index)
                time += protime  
            else:
               
                time = idx_task[i][0]
        
        return result