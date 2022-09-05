# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

import time
import math


try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys('dfsdfas')
    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys('dfsdfas')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('dgfdfsgd')
    btnchoose = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'first_script copy.txt')
    btnchoose.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button").click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

