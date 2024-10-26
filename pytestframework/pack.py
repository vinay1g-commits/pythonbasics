from selenium.webdriver.chrome.webdriver import WebDriver

from pytestframework.tests.test_search import driver


class test:
    driver = WebDriver.Chrome()
    driver.get("https://www.oneinidia.com")
def add(a,b):
    return a+b
result = add(2,3)
print(result)

def click():
    driver.fin

