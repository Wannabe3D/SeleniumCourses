import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


LOGIN = ''
PASSWORD = ''
LINKS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.mark.parametrize("link", LINKS)
def test_stepik(browser, link):
    browser.get(link)

    # Логинимся
    browser.find_element(By.CLASS_NAME,
                         "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
    browser.find_element(By.NAME, "login").send_keys(LOGIN)
    browser.find_element(By.NAME, "password").send_keys(PASSWORD)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

    # Ждём появления текстового поля ответа и вводим ответ
    answer_input = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
    answer_input.send_keys(math.log(int(time.time())))

    # Отправляем ответ
    submit_button = browser.find_element(By.CLASS_NAME, 'submit-submission')

    # Скроллим к ней
    browser.execute_script("arguments[0].scrollIntoView();", submit_button)

    # Кликаем через JavaScript (устойчивее к багам)
    browser.execute_script("arguments[0].click();", submit_button)

    # Проверяем фидбек
    feedback = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
    )
    feedback_text = feedback.text

    button1 = browser.find_element(By.CLASS_NAME, 'again-btn.white')
    button1.click()

    assert "Correct!" in feedback_text, f"Текст фидбека: '{feedback_text}', ожидалось: 'Correct!'"

if __name__ == "__main__":
    pytest.main()