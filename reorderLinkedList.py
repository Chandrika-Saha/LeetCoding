# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # If the linked list is empty or only has one node
        if not head or not head.next:
            return

        # Initialize the slow and fast linked list with the head, 
        # we want to find the spot to split the list
        slow, fast = head, head

        # As long as the fast and fast.next exist
        while fast and fast.next:
            slow = slow.next # Increment slow once
            fast = fast.next.next # Increment fast twice
            

        # Now, need to reverse the seson half of the list
        reverse = slow.next # Starting node of the second half of the list
        slow.next = None # Detach the first part of the linked list
        prev = None # This will help in reversing the list

        # As long as reverse exists
        while reverse:
            temp = reverse.next # Put the next node in a temp variable
            reverse.next = prev # This node will point to the node before it
            prev = reverse # Set the previous node to the current node
            reverse = temp # set the current next node to reverse node
        
        # get pointers for the first part of the unaltered list
        # and the second part, the reversed list
        first, second = head, prev
        while second: # As long as there are items left in the reversed part, keep rearranging
            temp1, temp2 = first.next, second.next # Keep copies of next nodes of both lists
            first.next = second # The first node now points to the last node
            second.next = temp1 # The node that was just attached after the head, now points to the node next to head
            first, second = temp1, temp2 # The next nodes of each lists are assigned to them

