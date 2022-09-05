# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

import time
import math
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    trollface_button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    y = calc(x)
    ans = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    ans.send_keys(y)
    btn = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

