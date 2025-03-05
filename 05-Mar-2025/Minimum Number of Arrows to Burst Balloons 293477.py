# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        print(points)
        n = len(points)
        arrow = 1
        prev = points[0][1]

        for i in range(1,n):
            if prev < points[i][0]:
                arrow += 1
                prev = points[i][1]
        return arrow
        