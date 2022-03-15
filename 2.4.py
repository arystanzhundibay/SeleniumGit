from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
try:
    price = browser.find_element(By.ID, 'price')
    wait = WebDriverWait(browser, 20)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()