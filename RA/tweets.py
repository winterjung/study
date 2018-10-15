import contextlib
import time
from datetime import date, timedelta
from urllib.parse import urlencode
from typing import Dict, Optional

from selenium import webdriver  # type: ignore
from selenium.webdriver.remote.webdriver import WebDriver  # type: ignore


def create_chrome_options(headless: bool = True):
    options = webdriver.ChromeOptions()
    path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    options.binary_location = path
    if headless:
        options.add_argument('headless')
    return options


@contextlib.contextmanager
def create_driver(browser: Optional[WebDriver] = None, options=None) -> WebDriver:
    if browser is None:
        browser = webdriver.Chrome
    try:
        driver = browser(options=options)
        yield driver
    finally:
        driver.quit()


def create_query(
    keyword: str, since: Optional[date] = None, until: Optional[date] = None
) -> Dict:
    if not keyword:
        raise ValueError('`keyword` should be filled')
    query = f'{keyword}'
    if since:
        query += f' since:{str(since)}'
    if until:
        query += f' until:{str(until)}'
    return dict(q=query)


def create_url(query: Dict) -> str:
    query_string = urlencode(query)
    url = f'https://twitter.com/search?{query_string}'
    return url


def handle_tweets(driver: WebDriver):
    """
    select -> refine -> extract
    """


def ensure_end(driver: WebDriver, threshold: int = 2) -> bool:
    return all(is_ended(*scroll(driver, 1)) for _ in range(threshold))


def scroll(driver: WebDriver, seconds: int = 1):
    prev_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(seconds)
    curr_height = driver.execute_script('return document.body.scrollHeight')
    return prev_height, curr_height


def is_ended(pre: int, cur: int) -> bool:
    return pre == cur


def scroll_timeline(driver: WebDriver, url: str):
    driver.get(url)
    while True:
        if is_ended(*scroll(driver)) and ensure_end(driver):
            break


def get_old_tweets(driver: WebDriver, keyword: str, since: date, until: date):
    now = since + timedelta(days=1)
    while now <= until:
        query = create_query(keyword, since, now)
        url = create_url(query=query)
        scroll_timeline(driver, url)
        handle_tweets(driver)
        now += timedelta(days=1)


def main():
    keyword = '미세먼지'
    since = date(2017, 10, 1)
    until = date(2017, 10, 2)
    options = create_chrome_options(headless=False)
    with create_driver(webdriver.Chrome, options) as driver:
        get_old_tweets(driver, keyword, since, until)


if __name__ == '__main__':
    main()
