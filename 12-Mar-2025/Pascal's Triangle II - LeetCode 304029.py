# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [1]
        arr = self.getRow(rowIndex - 1)

        for i in range(1,len(arr)):
            ans.append(arr[i] + arr[i - 1])
        ans.append(1)
        return ans
        