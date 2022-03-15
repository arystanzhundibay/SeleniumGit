from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys('Ivan')

    surname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    surname.send_keys('Petrov')

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('mail')

    file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
