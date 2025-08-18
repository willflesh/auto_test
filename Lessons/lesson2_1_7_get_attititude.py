from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(2)

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

link = browser.find_element(By.ID, 'answer')
link.send_keys(y)
time.sleep(2)

link2 = browser.find_element(By.ID, 'robotCheckbox')
link2.click()

link3 = browser.find_element(By.ID, 'robotsRule')
link3.click()
time.sleep(2)

link4 = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
link4.click()
time.sleep(4)
