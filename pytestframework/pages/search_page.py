# pages/search_page.py

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "searchInput")  # Update the locator with actual ID/Name
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.searchButton")  # Update with actual button selector

    def enter_search_term(self, term):
        self.enter_text(*self.SEARCH_INPUT, text=term)

    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)
