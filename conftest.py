import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en",
                     help="Choose language: ru, en, fr, ..")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
