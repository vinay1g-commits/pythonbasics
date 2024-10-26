# config/browsers.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.user_agents import MOBILE_USER_AGENT

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={MOBILE_USER_AGENT['chrome']}")
    chrome_options.add_argument("--window-size=375,812")  # iPhone X size
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.set_preference("general.useragent.override", MOBILE_USER_AGENT['firefox'])
    firefox_options.add_argument("--width=375")
    firefox_options.add_argument("--height=812")
    driver = webdriver.Firefox(options=firefox_options)
    return driver
