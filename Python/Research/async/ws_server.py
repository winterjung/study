import asyncio

import websockets


async def hello(websocket, path):
    print('path:', path)
    if path == '/':
        name = await websocket.recv()
        print("< {}".format(name))

        greeting = "Hello {}!".format(name)
        await websocket.send(greeting)
        print("> {}".format(greeting))
    else:
        age = await websocket.recv()
        print("< {}".format(age))

        greeting = "Hello your old is {}!".format(age)
        await websocket.send(greeting)
        print("> {}".format(greeting))


start_server = websockets.serve(hello, 'localhost', 8765)
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(start_server)
    loop.run_forever()
except KeyboardInterrupt:
    print("Close server")
    loop.close()
