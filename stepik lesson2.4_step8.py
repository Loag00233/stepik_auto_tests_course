# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    y = calc(x)
    ans = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    ans.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

