from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class WindowsPage(BasePage):
    NewTab = (By.XPATH, '//b[.="New Tab"]')
    ReplaceWindow = (By.XPATH, '//b[.="Replace Window"]')
    NewWindow = (By.XPATH, '//b[.="New Window"]')

    def __init__(self, driver):
        super().__init__(driver)  # Ensure proper inheritance

    def open_new_tab(self):
        self.driver.find_element(*self.NewTab).click()

    def open_replace_window(self):
        self.driver.find_element(*self.ReplaceWindow).click()

    def open_new_window(self):
        self.driver.find_element(*self.NewWindow).click()
