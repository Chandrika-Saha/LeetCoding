# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # If one of the list is empty, return the other list as the result
        if not (list1 or list2):
            return list1 if not list2 else list2

        # Initialze an empty list
        final_merged = ListNode()
        merged_list = final_merged

        # As long as there are items in both the list
        while list1 and list2:
            # If the value of list1 is smaller than list2, assign that in the new list
            if list1.val < list2.val:
                merged_list.next = list1
                list1 = list1.next # Move list1 ahead, this logic works because both lists are sorted
            else:
                # In case list2 value is smaller than or equal to list1 current value, assign that to the new list
                merged_list.next = list2
                list2 = list2.next # Move list2 ahead
            # Move the merged_list to the next node, which was added just now. To form the chain
            merged_list = merged_list.next 
        
        # If there are remaining list1, add them to the end of the new list
        if list1:
            merged_list.next = list1
        # If there are remaining list2, add them to the end of the new list
        if list2:
            merged_list.next = list2

        # Return the next of the final_merged which is the head of the merged list
        # We are returning the next node because the first node contains a zero
        return final_merged.next