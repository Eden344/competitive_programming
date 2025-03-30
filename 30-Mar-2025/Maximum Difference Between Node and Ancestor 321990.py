# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def tree(node, min_val, max_val):
            if not node:
                return max_val - min_val
            
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left_tree = tree(node.left, min_val, max_val)
            right_tree = tree(node.right, min_val, max_val)

            return max(left_tree, right_tree)
        return tree(root, root.val, root.val)