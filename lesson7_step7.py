import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим картинку сундука на странице и вытаскиваем из него значение
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # находим кнопки и кликаем на них
    checkbox_button = browser.find_element(By.ID, "robotCheckbox")
    checkbox_button.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

