from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
time.sleep(3)

browser.switch_to.window(browser.window_handles[1])

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

link = browser.find_element(By.ID, 'answer')
link.send_keys(y)

browser.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
