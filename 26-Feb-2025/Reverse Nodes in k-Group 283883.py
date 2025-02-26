# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp = head
        count = 0 
        while temp and count < k:
            temp = temp.next 
            count += 1
        
        if count < k:
            return head

        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverseKGroup(curr, k)

        return prev

        