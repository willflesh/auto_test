import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_google_search(browser):
    browser.get("http://google.com")

    assert "Google" in browser.title
    search_box = browser.find_element(By.NAME, "q")
    assert search_box.is_displayed()
    search_button = browser.find_element(By.NAME, "btnK")
    assert "Поиск в Google" in search_button.get_attribute("value")
