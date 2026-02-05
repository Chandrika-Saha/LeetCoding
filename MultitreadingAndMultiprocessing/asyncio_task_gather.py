import asyncio
import time


def timer(func):
    async def wrapper(*args, **kwargs):
        print(f"Starting funciton: {func.__name__!r}")
        start = time.time()
        res = await func(*args, **kwargs)
        print(f"Ending function: {func.__name__!r}, time took: {time.time()-start}")
        return res
    return wrapper

@timer
async def fetch_data(id, delay):
    print(f"Fetching data {id}")
    await asyncio.sleep(delay)
    print(f"data fetched {id}")
    return {"data": "sample data"}

@timer
async def main():
    print("Start of the coroutine")

    """This will take way longer to run, because we execute them one at a time anyway"""
    # f1 = fetch_data(1)
    # f2 = fetch_data(2)
    #
    # r1 = await f1
    # print(f"Received results: {r1}")
    #
    # r2 = await f2
    # print(f"Received results: {r2}")

    """This version uses task creation to make use of the idle time in between tasks"""
    # t1 = asyncio.create_task(fetch_data(1, 1))
    # t2 = asyncio.create_task(fetch_data(2, 2))
    # t3 = asyncio.create_task(fetch_data(3, 1.5))
    #
    # r1 = await t1
    # r2 = await t2
    # r3 = await t3
    #
    # print(r1, r2, r3)

    """Gather the tasks, less error handling, but the quickest to implement
    The gather will wait for all of them to finish, if one doesn't, too bad"""
    # results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1),
    #                          fetch_data(3, .5))
    #
    # print(f"The result: {results}")
    #
    # for res in results:
    #     print(f"Received result: {res}")

    """Task groups are better than the gather in the sense that it handles error in a
    coroutine, meaning, if one coroutine fails, it will fail the operation"""
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([1, 3, .5], start=1):
            task = tg.create_task(fetch_data(i, delay))
            tasks.append(task)

    results = [task.result() for task in tasks]
    print(f"The result is: {results}")

    print("End of the coroutine")


asyncio.run(main())