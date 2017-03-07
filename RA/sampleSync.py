import requests
from time import time


def fetch(page_num):
    print("Start", page_num)
    url = "http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno={}&orderby=docdatetime&c_scope=paging".format(
        page_num
    )
    response = requests.get(url)
    print("Done", page_num)
    return response.text


def fetch_all(start, end):
    fetches = [fetch(page_num) for page_num in range(start, end)]
    return fetches


start = time()
fetch_all(502, 505)
elapse = time() - start
print("elapse", elapse)
