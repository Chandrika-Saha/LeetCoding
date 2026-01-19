import multiprocessing_q

# Use shared memory to get around this limitation of not having
# shared memory between processes
result = []
def square(nums, pa, pv):
    global result
    for i, n in enumerate(nums):
        print("Square:", n**2)
        result.append(("Square", n**2))
        pa[i] = n**2
    # This is bytes literal of the string, this ensures we are treating all
    # characters as bytes, not the whole thing as a string
    pv.value = b"S"
    print(result)

def cube(nums, pa, pv, N):
    global result
    for i, n in enumerate(nums, start=N):
        print("Cube:", n**3)
        result.append(("Cube", n**3))
        pa[i] = n**3
    pv.value = b"C"
    print(result)

if __name__ == "__main__":
    arr = [1, 2, 3]

    # This Array is backed by shared memory; passing it to processes lets them read/write the same buffer.
    # They can only hold a specific data type, nothing fancy.
    # Need to have an indexing schema to properly store the values in the shared array
    # Need to pass the information about the indexing to keep the thing going, also need to have enough memory
    # to store everything, overall, not very flexible
    pa = multiprocessing.Array('i', len(arr)*2)

    # This value is shared and can only store trivial types, not good with strings too.
    pv = multiprocessing.Value('c', b"A")

    p1 = multiprocessing.Process(target=square, args=(arr, pa, pv))
    p2 = multiprocessing.Process(target=cube, args=(arr, pa, pv, len(arr)))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finish line")
    print("This is the value:", pv.value)
    print("This is the shared array:", pa[:])
    print("Resultssss:", result)
