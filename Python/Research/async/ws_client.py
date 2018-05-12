import asyncio

import websockets


async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


async def my_age():
    async with websockets.connect('ws://localhost:8765/custom_path') as websocket:
        age = input("What's your age? ")
        await websocket.send(age)
        print("> {}".format(age))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


tasks = asyncio.gather(hello(), my_age())
asyncio.get_event_loop().run_until_complete(tasks)
