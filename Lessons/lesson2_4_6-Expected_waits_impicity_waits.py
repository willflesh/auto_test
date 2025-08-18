# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# В модуле expected_conditions есть много других правил,
# которые позволяют реализовать необходимые ожидания:
#
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
browser.find_element(By.CSS_SELECTOR, 'button#book').click()

button = browser.find_element(By.ID, 'solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

link1 = browser.find_element(By.ID, 'answer')
link1.send_keys(y)
time.sleep(2)
link2 = browser.find_element(By.ID, 'solve')
link2.click()
time.sleep(3)
