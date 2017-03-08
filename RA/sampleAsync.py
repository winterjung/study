import json
from time import time
from collections import OrderedDict
from bs4 import BeautifulSoup
# Async 모듈
import aiohttp
import asyncio


result = OrderedDict()


async def fetch(page_num):
    print("Start", page_num)
    url = "http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno={}&orderby=docdatetime&c_scope=paging".format(
        page_num
    )
    response = await aiohttp.request("GET", url)
    print("Done", page_num)
    text = await response.text()
    html = text
    soup = BeautifulSoup(html, "html.parser")
    news_result = soup.select("#result > div.result_box > section > dl")

    for news in news_result:
        date = news.select("em")[0].get_text()
        title = news.select("dt > a")[0].get_text()
        category = news.select("a")[-1].get_text()
        url = news.select("dt > a")[0]["href"]
        content_id = url.split("contid=")[-1]
        if len(content_id) > 13:
            content_id = url.split("/")[-1][:13]
        result[content_id] = {
            "title": title,
            "date": date,
            "category": category,
            "text": None,
            "url": url,
        }
    print(len(result))
    return text


async def fetch_all2(start, end):
    fetches = [asyncio.Task(fetch(page_num)) for page_num in range(start, end)]
    await asyncio.gather(*fetches)


async def fetch_all(start, end):
    fetches = []
    for page_num in range(start, end):
        fetches.append(asyncio.Task(fetch(page_num)))
        await asyncio.sleep(0.3)
    await asyncio.gather(*fetches)


loop = asyncio.get_event_loop()
start = time()
loop.run_until_complete(fetch_all(502, 571))
elapse = time() - start
loop.close()
print("elapse", elapse)

with open("sample_003.json", mode="w", encoding="utf-8") as fp:
    json.dump(
        result,
        fp,
        ensure_ascii=False,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )
    # fp.write(str(result))
