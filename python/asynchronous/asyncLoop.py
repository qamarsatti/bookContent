import asyncio

async def count():
    # print("One")
    await asyncio.sleep(4)
    print("Two")

async def main():
    l=[count()]
    for _ in range(1,1000):
        l.append(count())
    await asyncio.gather(*l)

asyncio.run(main())   