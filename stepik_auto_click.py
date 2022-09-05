# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
email = '33200goal@gmail.com'
pas = 'Motcart12'

try:
    browser = webdriver.Chrome()
    link = "https://stepik.org/catalog?auth=login"
    browser.get(link)
    time.sleep(4)
    # visible_button = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.TAG_NAME, "img"))) #не стал использовать Wait - почему то отрабатывает дольше sleep

    browser.find_element(By.ID, "id_login_email").send_keys(email)
    browser.find_element(By.ID, "id_login_password").send_keys(pas)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

    #переходим на страницу теста
    browser.get('https://stepik.org/lesson/236205/step/2?unit=208637')



    # browser = webdriver.Chrome()
    # link = "http://suninjuly.github.io/explicit_wait2.html"
    # browser.get(link)
    # price = WebDriverWait(browser, 12).until(
    #     EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    # book_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    # x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    # y = calc(x)
    # ans = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    # ans.send_keys(y)
    # submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

