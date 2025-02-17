from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait for elements
    return driver
