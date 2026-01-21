from minheap import MinHeap
class MaxHeap:
    def __init__(self):
        self.heap = MinHeap()

    def push(self, val):
        self.heap.push(-val)

    def pop(self):
        return -self.heap.pop()

    def peek(self):
        return -self.heap.peek()


import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)

print(heapq.heappop(heap))  # 1
