# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(arr):
            l , r = 0 , len(arr) - 1
            while l < r:
                arr[l].val , arr[r].val = arr[r].val , arr[l].val
                l+=1
                r-=1
            

        if not root:
            return []
      
        que = deque([(root, 0 )])

        while que:
            n = len(que)
            ans = []

            for _ in range(n):
                node ,lvl= que.popleft()

                if lvl% 2!=0:
                    ans.append(node)


                if node.left:
                    que.append((node.left, lvl + 1))
                if node.right:
                    que.append((node.right, lvl + 1))
            if ans:
                reverse(ans)
           
        return root
            