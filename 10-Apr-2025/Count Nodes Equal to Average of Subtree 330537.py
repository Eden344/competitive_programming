# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def tree(node):
            if not node:
                return (0,0)

            left_sum, left_count = tree(node.left)
            right_sum, right_count = tree(node.right)


            summ = left_sum + right_sum + node.val
            sub_count = left_count + right_count + 1

            if node.val == summ//sub_count:
                self.count += 1

            return (summ, sub_count)

        tree(root)
        return self.count