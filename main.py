from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button

browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/button/simple')

# click_botton = browser.find_element(By.ID, 'submit-id-submit')
# click_botton.click()
# click_botton2 = browser.find_element(By.CLASS_NAME, 'btn')
# click_botton2.click()

link = browser.find_element(By.LINK_TEXT, 'Contact')
link.click()
time.sleep(5)

# click_button3 = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
# click_button3.click()
# time.sleep(5)

# click_button4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
# click_button4.click()
# time.sleep(5)
