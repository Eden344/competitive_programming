# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    def __init__(self):
        self.lower_half = []  
        self.upper_half = []  

    def addNum(self, num: int) -> None:
     
        heapq.heappush(self.lower_half, -num)
        
        if (self.lower_half and self.upper_half and 
            (-self.lower_half[0] > self.upper_half[0])):
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)

       
        if len(self.lower_half) > len(self.upper_half) + 1:
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)
        elif len(self.upper_half) > len(self.lower_half):
            val = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -val)

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])
        else:
            return (-self.lower_half[0] + self.upper_half[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()