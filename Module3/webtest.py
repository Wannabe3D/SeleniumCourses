import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestWeb(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fill_form_and_submit(self, link):
        self.browser.get(link)

        self.browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[required]').send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[required]').send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[required]').send_keys("example@mail.ru")

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        return self.browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_form_and_submit(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Registration failed on page 1")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_form_and_submit(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Registration failed on page 2")


if __name__ == "__main__":
    unittest.main()