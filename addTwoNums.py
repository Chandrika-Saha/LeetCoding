# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = "", ""

        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next

        result = str(int(num1[::-1]) + int(num2[::-1]))
        result = result[::-1]

        result_list = ListNode(int(result[0]))
        curr = result_list

        for char in result[1:]:
            temp = ListNode(int(char))
            curr.next = temp
            curr = temp

        return result_list
