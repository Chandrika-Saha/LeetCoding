# Each node contain the key and the value 
# All the entries are kept in between the left and the right node in a doubly linked list
# The left node represents the least recently used node while the right pointer showes the most recently used node
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    # We define the capacity of the DS
    # Define left and right pointers and connect them together
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    # This method inserts the new node near the right node
    # because it has been recently used
    def insert(self, node):
        p, n = self.right.prev, self.right
        p.next, n.prev = node, node
        node.prev, node.next = p, n

    # This method deletes the node that has just been accessed
    # to add it to the right of the list
    def delete(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    # Get the value for a given key
    # If the key is in the dictionary, delete the corresponding node from the list and 
    # add it near the right of the list since it has been accessed right now
    # Otherwise, return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    # Add the new key value in the dictionary   
    # If the key is in the dictionary, we need to delete that first
    # Then, create a new node, add it to the dictionary and insert it near the right
    # Also, need to check if capacity is exceeding. If it is, delete the node near left node
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)