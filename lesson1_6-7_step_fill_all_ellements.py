from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements(By.TAG_NAME, 'input')
for element in elements:
    element.send_keys("ITS A FAKE")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(7)
# закрываем браузер после всех манипуляций
browser.quit()
