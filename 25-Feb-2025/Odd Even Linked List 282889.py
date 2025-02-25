# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        start = even


        while even != None and odd != None and even.next != None and odd.next != None:

            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = start

        return head