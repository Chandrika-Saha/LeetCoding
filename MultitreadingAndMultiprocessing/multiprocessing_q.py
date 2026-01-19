import multiprocessing

# Use shared memory to get around this limitation of not having
# shared memory between processes
result = []
SENTINEL = None
def square(nums, q):
    global result
    for i, n in enumerate(nums):
        print("Square:", n**2)
        result.append(("Square", n**2))
        q.put(("Square", n**2))
    # Need to add this at the end of the queue to properly handle the end of the queue
    q.put(SENTINEL)
    print(result)

def cube(q, o):
    global result
    # So, we keep waiting for items in the queue.
    # If the queue not empty, doesn't mean it can't have items coming in.
    # The SENTINEL is the only thing that marks the end of the queue.
    while True:
        # When we use get, we essentially remove the item from the queue
        n = q.get()
        if n is SENTINEL:
            break
        result.append(("Cube", n[1]**3))
        o.put(("Cube", n[1]**3))
    o.put(SENTINEL)
    print(result)

if __name__ == "__main__":
    arr = [1, 2, 3]

    q = multiprocessing.Queue()
    o = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square, args=(arr, q))
    p2 = multiprocessing.Process(target=cube, args=(q, o))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finish line")

    print("Resultssss:")
    while True:
        n = o.get()
        if n is SENTINEL:
            break
        print(n)


