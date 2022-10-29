import asyncio
import time

import aiohttp
import requests
from tqdm import tqdm


async def async_gather_http_get(url, path: str, times: int):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in tqdm(range(times), desc='Async gather fetching data...', colour='GREEN'):
            tasks.append(asyncio.create_task(session.get(url + path)))

        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]




if __name__ == '__main__':
    N = 10
    api = 'salexy.kg'

    start_timestamp = time.time()
    print(async_gather_http_get(api,path='fact/', times=N))

    task_time = round(time.time() - start_timestamp, 2)
    rps = round(N / task_time, 1)
    print(
        f"| Requests: {N}; Total time: {task_time} s; RPS: {rps}. |\n"
    )