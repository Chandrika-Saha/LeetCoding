"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Create a dictionary to store the new nodes corresponding to the current node
        node_mapping = {None: None}

        # Start from the head
        curr = head
        while curr:
            # Create a copy of each of the nodes of the linked list, with only the values
            temp = Node(curr.val)
            # Map the new node to the old node
            node_mapping[curr] = temp
            # Increment the current pointer
            curr = curr.next

        # This is pass 2, start with the head of the original linked list
        curr = head
        while curr:
            # Get the copy of the node 
            new = node_mapping[curr]
            # Make the necessary connections
            new.next = node_mapping[curr.next]
            new.random = node_mapping[curr.random]
            curr = curr.next

        # Return the head of the new list
        return node_mapping[head]
            

        return deepcopy.next