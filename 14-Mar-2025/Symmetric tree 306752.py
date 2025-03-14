# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       
        def tree( one, two):
            if  (not one )and (not two):
                return True
            if one and (not two):
                return False
            if (not one) and two:
                return False

            val = one.val == two.val
            ans = tree(one.left, two.right)
            ans2 = tree(one.right, two.left)
            return ans and ans2 and val
        return tree(root.left, root.right)
            

               
        