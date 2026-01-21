from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---- Example Usage ----
q = Queue()

q.enqueue(5)
q.enqueue(10)
q.enqueue(15)

print("Queue size:", q.size())    # 3
print("Front element:", q.peek()) # 5

print("Dequeued:", q.dequeue())   # 5
print("Front after dequeue:", q.peek())  # 10
