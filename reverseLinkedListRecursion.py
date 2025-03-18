# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case, occurs when we reach the last node
        if not head:
            return None
        
        # Initially will contain the last node, because base case will be the last node
        # It will then recursively add the other nodes, this is essentially the tail of the linked list
        newHead = head
        
        # If there is still a node to explore
        if head.next:
            # This holds last node first, and builds starting with that
            newHead = self.reverseList(head.next)
            # This is where the reverse happen. The next pointer of the tail is pointing back to the previous node
            head.next.next = head
        # The node which was just pointed by the previous node to reverse the list points to None.
        # Because it essentially is the tail of the reversed list
        head.next = None

        return newHead # This is the last node of the original list and the new head of the reversed list