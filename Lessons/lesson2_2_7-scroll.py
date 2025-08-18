from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

link = browser.find_element(By.ID, 'answer')
link.send_keys(y)

link2 = browser.find_element(By.ID, 'robotCheckbox')
link2.click()

link3 = browser.find_element(By.ID, 'robotsRule')
link3.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(3)
