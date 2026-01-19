import multiprocessing


# def deposite(m, v, l):
#     for i in range(m):
#         l.acquire()
#         v.value += 1
#         l.release()

def deposit(m, v):
    for _ in range(m):
        with v.get_lock():
            v.value += 1


# def withdraw(m, v, l):
#     for i in range(m):
#         l.acquire()
#         v.value -= 1
#         l.release()

def withdraw(m, v, l):
    for i in range(m):
        with v.get_lock():
            v.value -= 1



if __name__ == "__main__":
    v = multiprocessing.Value('i', 200)
    l = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=deposit, args=(100, v))
    p2 = multiprocessing.Process(target=withdraw, args=(200, v, l))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("The final value:", v.value)

