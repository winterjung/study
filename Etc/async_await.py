import asyncio
import aiohttp
from typing import List

Response = aiohttp.client_reqrep.ClientResponse


async def fetch(session: aiohttp.ClientSession, url: str) -> Response:
    async with session.get(url) as response:
        print(f"request {url}")
        return response


async def fetch_all(urls: List[str]) -> Response:
    requests = [asyncio.Task(fetch(url)) for url in urls]
    result = await asyncio.gather(*requests)
    return result


async def sleep(time: int) -> None:
    await asyncio.sleep(time)


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        res: Response = await fetch(session, "http://google.com")
        print(res.status)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
