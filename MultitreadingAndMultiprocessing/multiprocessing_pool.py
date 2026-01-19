import multiprocessing


def f(n):
    return n*n

if __name__ == "__main__":

    p = multiprocessing.Pool(processes=3)

    result = p.map(f, [1, 2, 3, 4])

    for n in result:
        print(n)

