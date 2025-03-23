# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # The single node is deleted
        # If there is only one node, based on the constraints we can simply return None.
        if not head.next:
            return None
        
        # Go over the entire linked list to count the number of nodes
        curr = head
        count = 0

        # Count all the nodes until the end
        while curr:
            curr = curr.next
            count += 1

        # Target the the number of node we have to delete, 
        # if we are starting from the head of the linked list
        target = count - n

        # Once again, we iterate over the list until we reach 'target' number of node
        curr = head
        count = 1

        # As long as the count is less than the target, we increment
        while count < target:
            curr = curr.next
            count += 1

        # Now, for the case of a linked list of length 'n' where we want to delete the 'n'th node
        # That n'th node is nothing but the head of the linked list, so we simply increment that
        if curr == head and target == 0:
            head = head.next
        else: 
        # For all other cases, we found the node before the target node, 
        # and we link it to the node after the target node
            curr.next = curr.next.next

        # In the end, we return the head
        return head