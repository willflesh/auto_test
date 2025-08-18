from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.CSS_SELECTOR, '.nowrap#num1')
y = browser.find_element(By.CSS_SELECTOR, '.nowrap#num2')
x = int(x.text)
y = int(y.text)
summa = str(x + y)
time.sleep(1)

select_el = browser.find_element(By.CLASS_NAME, 'custom-select')
select = Select(select_el)
select.select_by_value(summa)
time.sleep(1)

click = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
click.click()
time.sleep(2)
