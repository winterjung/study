import requests
from time import time
# Async 모듈
import aiohttp
import asyncio


@asyncio.coroutine
def fetch(page_num):
    print("Start", page_num)
    url = "http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno={}&orderby=docdatetime&c_scope=paging".format(
        page_num
    )
    response = yield from aiohttp.request("GET", url)
    print("Done", page_num)
    return (yield from response.text())


@asyncio.coroutine
def fetch_all(start, end):
    fetches = [asyncio.Task(fetch(page_num)) for page_num in range(start, end)]
    yield from asyncio.gather(*fetches)


loop = asyncio.get_event_loop()
start = time()
loop.run_until_complete(fetch_all(502, 505))
elapse = time() - start
loop.close()
print("elapse", elapse)
