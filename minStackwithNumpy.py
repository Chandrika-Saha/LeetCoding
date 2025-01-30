import numpy as np
class MinStack:

    def __init__(self):
        self.stack = np.array([], dtype='int32')
        self.minimum = np.array([], dtype='int32')

    def push(self, val: int) -> None:
        self.stack = np.append(self.stack, val)
        val = min(val, self.minimum[-1] if self.minimum.size > 0 else val)
        self.minimum = np.append(self.minimum, val)

    def pop(self) -> None:
        if self.stack.size > 0:
            popped = self.stack[-1]
            self.stack = self.stack[:-1]
            self.minimum = self.minimum[:-1]
        return int(popped)

    def top(self) -> int:
        return int(self.stack[-1]) if self.stack.size > 0 else []

    def getMin(self) -> int:
        return int(self.minimum[-1]) if self.minimum.size > 0 else []

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(3)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()