class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        # Case 1: insert at head (position 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        current_pos = 0

        # Traverse to node just before the desired position
        while temp and current_pos < position - 1:
            temp = temp.next
            current_pos += 1

        # If position is out of bounds
        if not temp:
            raise IndexError("Position out of bounds")

        # Insert node
        new_node.next = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head

        # Case 1: deleting head
        # key = 3
        # 1 -> 2 -> 3 -> 4
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Case 2: delete in the middle or end
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:  # found node
            prev.next = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Create list
ll = LinkedList()

# Insert elements
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.print_list()
# Output: 20 -> 10 -> 30 -> 40 -> None

# Search
print(ll.search(30))   # True
print(ll.search(100))  # False

# Delete
ll.delete(10)
ll.print_list()
# Output: 20 -> 30 -> 40 -> None

ll.insert_at_position(25, 2)
ll.print_list()
# 20 -> 10 -> 25 -> 30 -> 40 -> None

ll.insert_at_position(5, 0)
ll.print_list()
# 5 -> 20 -> 10 -> 25 -> 30 -> 40 -> None
