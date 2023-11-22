# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev = None
        # curr = head 

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # return prev

        # if not head:
        #     return None
        
        # newHead = head

        
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head

        # head.next = None
        
        # return newHead

        def reverse(curr, prev):

            if curr is None:
                return prev
            
            tempNode = curr.next
            curr.next = prev
            return reverse(tempNode, curr)
        

        return reverse(head, None)

        
            

        
