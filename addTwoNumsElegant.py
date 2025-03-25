# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the final linked list with the result of addition
        result = ListNode()
        dummy = result
        
        carry = 0 # Carry bit is initally 0
        while l1 or l2: # As long as either list exists
            # Get the digits from both lists if they exist, otherwise set 0
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0    

            # Adding digits and the carry
            add = a + b + carry
            carry = add // 10 # Updating carry
            add = add % 10 # Updating addition 

            # Create new node with the addition 
            node = ListNode(add)
            dummy.next = node # Attach it to the result
            dummy = node
        
            # Increment both list if they have nodes left
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If the carry was not 0, we still need to add that as one of the resultant digits
        if carry != 0:
            node = ListNode(carry)
            dummy.next = node
            dummy = node

        return result.next # Return the result.next