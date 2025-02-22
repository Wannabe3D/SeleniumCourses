import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим числа, которые нужно сложить
    x_element = browser.find_element(By.ID, 'num1').text
    y_element = browser.find_element(By.ID, 'num2').text

    # складываем значения, находим панель выбора и выбираем по результату
    result = int(x_element) + int(y_element)
    select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(f'{result}')

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

