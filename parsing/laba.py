import datetime
import time
import asyncio
async def foo():
    print('foo')
    time.sleep(2)
    print('foo2')
async def bar():
    print('bar')
    time.sleep(5)
    print('bar2')

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())

    await task1
    await task2


start_time = datetime.datetime.now()
# do your work here
print(start_time.time())

asyncio.run(main())
end_time = datetime.datetime.now()
print(end_time.time())


