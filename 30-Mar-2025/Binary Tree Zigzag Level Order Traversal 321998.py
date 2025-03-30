# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
       
        if not root:
            return []
        
        res = []
        que = deque([root])
        left_right = True

        while que:
            size = len(que)
            value = deque()

            for _ in range(size):
                node = que.popleft()

                if left_right:
                    value.append(node.val)
                else:
                    value.appendleft(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            res.append(list(value))
            left_right = not left_right
        return res




        