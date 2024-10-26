# tests/test_search.py
import pytest
from pytestframework.config import BASE_URL_EN, BASE_URL_HI
from pytestframework.pages.search_page import SearchPage
from pytestframework.config.browsers import get_chrome_driver

@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()

def test_search_functionality_oneindia_en(driver):
    driver.get(BASE_URL_EN)
    search_page = SearchPage(driver)
    search_page.enter_search_term("news")
    search_page.click_search_button()
    assert "results" in driver.current_url, "Search failed!"

def test_search_functionality_oneindia_hi(driver):
    driver.get(BASE_URL_HI)
    search_page = SearchPage(driver)
    search_page.enter_search_term("समाचार")
    search_page.click_search_button()
    assert "results" in driver.current_url, "Search failed!"
