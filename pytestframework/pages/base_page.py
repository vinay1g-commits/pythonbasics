# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def enter_text(self, *locator, text):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)
