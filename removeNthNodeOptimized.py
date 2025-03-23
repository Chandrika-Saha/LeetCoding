# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # The dummy node is here to keep track of the node right before the node that has to be deleted
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Create the gap between the left and the right nodes.
        # This gap should be equal to 'n'
        while right and n > 0:
            right = right.next
            n -= 1

        # As long as we can move the right pointer, we keep going
        while right:
            left = left.next
            right = right.next

        # After we are done, connect the node before the target node to the node after the target node
        left.next = left.next.next

        # In the end, return the modifed linked list
        return dummy.next
        