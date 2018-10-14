import contextlib
import time

from selenium import webdriver


def create_chrome_options(headless=True):
    options = webdriver.ChromeOptions()
    path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    options.binary_location = path
    if headless:
        options.add_argument('headless')
    return options


@contextlib.contextmanager
def create_driver(browser=None, options=None):
    if browser is None:
        browser = webdriver.Chrome
    try:
        driver = browser(options=options)
        yield driver
    finally:
        driver.quit()


def main():
    options = create_chrome_options()
    with create_driver(webdriver.Chrome, options) as driver:
        pass


if __name__ == '__main__':
    main()
