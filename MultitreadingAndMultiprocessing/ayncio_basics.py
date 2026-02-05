import asyncio

async def fetch_data(delay):
    print(f"Fetching data")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"data": "sample data"}
async def main():
    print("Start of the coroutine")
    f = fetch_data(1)
    res = await f
    print("End of the coroutine")
    print(f"Received results: {res}")

asyncio.run(main())