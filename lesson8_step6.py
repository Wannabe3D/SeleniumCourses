import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим и просчитываем значение, вводим в поле, скроллим страницу вниз
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")

    # находим кнопки и кликаем на них
    checkbox_button = browser.find_element(By.ID, "robotCheckbox")
    checkbox_button.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

