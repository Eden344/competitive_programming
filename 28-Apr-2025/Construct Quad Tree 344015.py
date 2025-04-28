# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(x, y, length):
            first_value = grid[x][y]
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != first_value:
                        return False, None
            return True, first_value

        def buildTree(x, y, length):
            uniform, value = isUniform(x, y, length)
            if uniform:
                return Node(val=bool(value), isLeaf=True)
            else:
                half = length // 2
                node = Node(val=False, isLeaf=False)
                node.topLeft = buildTree(x, y, half)
                node.topRight = buildTree(x, y + half, half)
                node.bottomLeft = buildTree(x + half, y, half)
                node.bottomRight = buildTree(x + half, y + half, half)
                return node

        return buildTree(0, 0, len(grid))
        