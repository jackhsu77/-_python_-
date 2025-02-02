import asyncio
import sys

t = {}
t["1"] = 111
t["2"] = 222
for v in t.keys():
    print(f" --> {v}")
t = []
t.append(123)
t.append(456)
for v in t:
   print(f" --> {v}")
sys.exit()

async def fetch_data(delay, data):
    print(f"Start fetching {data}")
    await asyncio.sleep(delay)
    print(f"Finished fetching {data}")
    return data

async def main():
    task1 = asyncio.create_task(fetch_data(2, "data1"))
    task2 = asyncio.create_task(fetch_data(3, "data2"))
    task3 = asyncio.create_task(fetch_data(1, "data3"))
    #results = await asyncio.gather(task1, task2, task3)
    #print(f"Results: {results}")
    a = await task1
    print(task1.result())
    a = await task2
    print(task2.result())
    a = await task3
    print(task3.result())
asyncio.run(main())

print(12345)

