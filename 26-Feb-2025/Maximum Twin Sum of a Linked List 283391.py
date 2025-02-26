# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left = head
        right = prev
        maxi = 0

        while right:
            summ = left.val + right.val
            maxi = max(maxi, summ)
            left = left.next
            right = right.next
        return maxi

        



        
        