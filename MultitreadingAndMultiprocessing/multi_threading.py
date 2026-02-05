import threading
import time

def calc_square(nums):
    print("Calculating square numbers")
    for n in nums:
        time.sleep(1)
        print("Square:", n**2)

def calc_cube(nums):
    print("Calculate cube of numbers")
    for n in nums:
        time.sleep(1)
        print("Cube:", n**3)

arr = [2, 3, 4, 5]

# Multi-treading in Python follow the GIL (Global Interpreter Lock), that make the interpreter use only
# one CPU until am I/O thing is prompted. So, we use multi-threading for I/O bound load and
# multiprocessing for CPU bound loads.

t = time.time()

calc_square(arr)
calc_cube(arr)

print("Done in: ", time.time() - t)

tt = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Threading done in: ", time.time()-tt)





