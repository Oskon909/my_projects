import asyncio

# async def count_to_three():
#     print("Веду отсчёт. 1")
#     await asyncio.sleep(0)
#     print("Веду отсчёт. 2")
#     await asyncio.sleep(0)
#     print("Веду отсчёт. 3")
#     await asyncio.sleep(0)
# coroutine_counter = count_to_three()
# print(coroutine_counter)
# coroutine_counter.send(None)
# coroutine_counter.send(None)
# coroutine_counter.send(None)



async def count(limit=3):
    for step in range(1, limit+1):
        print("Веду отсчёт.", step)
        await asyncio.sleep(0)

coroutine = count(5)

while True:
    try:
        coroutine.send(None)
    except StopIteration:
        break