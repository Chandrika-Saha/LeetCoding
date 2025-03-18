# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointers
        prev, curr = None, head

        # As long as curr is not None
        while curr:
            temp = curr.next # Keep a copy of the next node
            curr.next = prev # Assign next of curr to the previous node, 
            prev = curr # Assing current node as the previous node
            curr = temp # Move current to the next node

        return prev # Return previous since it contain the head node of the reversed list