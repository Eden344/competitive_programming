# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = 100000 
        fenwick_tree = FenwickTree(max_val)
        total_cost = 0

        for i in range(len(instructions)):
            current = instructions[i]
           
            count_less = fenwick_tree.query(current - 1)
            
            count_greater = i - fenwick_tree.query(current)
            
            total_cost += min(count_less, count_greater)
            total_cost %= MOD
            fenwick_tree.update(current, 1)

        return total_cost

