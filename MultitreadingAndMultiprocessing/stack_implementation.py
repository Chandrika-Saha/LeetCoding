## In this code we will implement a Stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---- Example Usage ----
s = Stack()

s.push(5)
s.push(10)
s.push(15)

print("Stack size:", s.size())      # 3
print("Top element:", s.peek())     # 15

print("Popped:", s.pop())           # 15
print("Top after pop:", s.peek())   # 10
