
import asyncio
import time


async def waiter() -> None:
    await cook('Паста', 8)
    await cook('Салат Цезарь', 3)
    await cook('Отбивные', 16)


async def cook(order: str, time_to_prepare: int) -> None:
    print(f'Новый заказ: {order}')
    time.sleep(time_to_prepare)
    print(order, '- готово')




asyncio.run(waiter())
