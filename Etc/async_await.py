import asyncio
import aiohttp
import timeit
from typing import List

Response = aiohttp.client_reqrep.ClientResponse


async def fetch(session: aiohttp.ClientSession, url: str) -> Response:
    async with session.get(url) as response:
        print(f"request {url}")
        return response


async def fetch_with_sleep(session: aiohttp.ClientSession,
                           url: str,
                           sleep_time: int) -> Response:
    async with session.get(url) as response:
        print(f"request {url} with {sleep_time}s")
        await sleep(sleep_time)
        print(f"request {url} sleep done")
        return response


async def sleep(time: int) -> None:
    await asyncio.sleep(time)


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        res: Response = await fetch(session, "http://google.com")
        print(res.status)


async def main_2() -> None:
    async with aiohttp.ClientSession() as session:
        print("Fetch 1")
        await fetch(session, "http://google.com")
        print("Fetch 2")
        await fetch(session, "http://python.org")

        # Fetch 1
        # request http://google.com
        # Fetch 2
        # request http://python.org
        # duration: 2.6572424746573597


async def main_3() -> None:
    async with aiohttp.ClientSession() as session:
        print("Fetch 1")
        await fetch_with_sleep(session, "http://google.com", 5)
        print("Fetch 2")
        await fetch_with_sleep(session, "http://python.org", 2)

        # Fetch 1
        # request http://google.com with 5s
        # request http://google.com sleep done
        # Fetch 2
        # request http://python.org with 2s
        # request http://python.org sleep done
        # duration: 9.417719859595575


async def main_4() -> Response:
    async with aiohttp.ClientSession() as session:
        requests = [asyncio.Task(fetch_with_sleep(session,
                                                  "http://google.com",
                                                  5)),
                    asyncio.Task(fetch_with_sleep(session,
                                                  "http://python.org",
                                                  2))]
        result = await asyncio.gather(*requests)
        return result

        # request http://google.com with 5s
        # request http://python.org with 2s
        # request http://python.org sleep done
        # request http://google.com sleep done


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start = timeit.default_timer()
    loop.run_until_complete(main_2())
    duration = timeit.default_timer() - start

    print(f"duration: {duration}")
