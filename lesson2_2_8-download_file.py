import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('test_file.txt', 'w') as file:
    file.write('wassap')

link = "http://suninjuly.github.io/file_input.html"
com = webdriver.Chrome()
com.get(link)

firstname = com.find_element(By.NAME, "firstname").send_keys("VLD")

lastname = com.find_element(By.NAME, "lastname").send_keys("VLD")

num1 = com.find_element(By.NAME, "email").send_keys("vldk")

file_path = os.path.abspath('test_file.txt')
file_input = com.find_element(By.ID, 'file')
file_input.send_keys(file_path)

num2 = com.find_element(By.CLASS_NAME, "btn.btn-primary")
num2.click()
time.sleep(2)
