#!/usr/bin/env python

import asyncio
import websockets
#!/usr/bin/env python

import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8000") as websocket:
        await websocket.send("Hello world!")
        dddd=await websocket.recv()
        print(dddd)

asyncio.run(hello())