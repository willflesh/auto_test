import pytest
from selenium import webdriver
import tempfile
import shutil


def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en",
                     help="Choose language: ru, en, fr, ..")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = ChromeOptions()
    options.add_argument("--no-sandox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    user_data_dir=tempfile.mkdtemp()
    options.add_arguments(f"--user-data-dir={user_data_dir}")
    browser=webrdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    shutil.rmtree(user_data_dir)
