import asyncio
import websockets
import chatgpt

async def hello(websocket):
    query = await websocket.recv()
    print(f"<<< {query}")

    reply = chatgpt.meaning_of_life(query)

    await websocket.send(reply)
    print(f">>> {reply}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())