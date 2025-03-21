# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # If it's an empty linked list, return False 
        if not head:
            return False

        # Initialize slow with head and the fast with the next node
        slow, fast = head, head.next

        # As long as the fast is not a null node and there is a node following fast, continue
        # If either one of these is null, then we know that we have reached the end of the list
        # and there are no cycles in the linked list
        while fast and fast.next:

            # If there slow and fast matches, that means we have a cycle in the linked list
            # Even though fast is going two steps at a time, it will eventually catch up to slow if there is a cycle
            if slow == fast:
                return True

            # Increment slow one point
            # And increment fast two points for the algorithm to work
            slow = slow.next
            fast = fast.next.next

        # Return false in the end because no cycle exists
        return False