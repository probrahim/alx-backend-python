import asyncio

async def main():
    async def async_func(stop):
        for i in range(stop):
            yield i
            await asyncio.sleep(0)

    result = [i async for i in async_func(23) if i % 2]
    print(result)

asyncio.run(main())