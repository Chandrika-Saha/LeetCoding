# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        curr = head 

        count2 = count // 2 + 1

        i = 0
        while curr:
            i += 1
            if count2 == i:
                return curr
            curr = curr.next

        return None

