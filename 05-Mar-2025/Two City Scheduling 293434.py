# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda c: c[0] -c[1])
        print(costs)

        summ = 0
        n = len(costs)//2

        for i in range(n):
            summ += costs[i][0]
        for i in range(n, 2*n):
            summ += costs[i][1]
        return summ
