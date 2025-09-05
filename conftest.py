import pytest
from selenium import webdriver




def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en",
                     help="Choose language: ru, en, fr, ..")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito") 
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
